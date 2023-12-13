import torch
from collections import Counter
import os
import json
import csv
import glob
import pandas as pd
import numpy as np
from pathlib import Path
# import iou
# from iou import intersection_over_union

def compute_ap(recall, precision):
    """ Compute the average precision, given the recall and precision curves
    # Arguments
        recall:    The recall curve (list)
        precision: The precision curve (list)
    # Returns
        Average precision, precision curve, recall curve
    """

    # Append sentinel values to beginning and end
    mrec = np.concatenate(([0.], recall, [recall[-1] + 0.01]))
    mpre = np.concatenate(([1.], precision, [0.]))

    # Compute the precision envelope
    mpre = np.flip(np.maximum.accumulate(np.flip(mpre)))

    # Integrate area under curve
    method = 'interp'  # methods: 'continuous', 'interp'
    if method == 'interp':
        x = np.linspace(0, 1, 101)  # 101-point interp (COCO)
        ap = np.trapz(np.interp(x, mrec, mpre), x)  # integrate
    else:  # 'continuous'
        i = np.where(mrec[1:] != mrec[:-1])[0]  # points where x axis (recall) changes
        ap = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])  # area under curve

    return ap, mpre, mrec

def box_iou(boxA, boxB):
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)
	# return the intersection over union value
	return iou
def mean_average_precision(
    pred_boxes, true_boxes, iou_threshold=0.5, box_format="midpoint", num_classes=1
):
    """
    Calculates mean average precision 
    Parameters:
        pred_boxes (list): list of lists containing all bboxes with each bboxes
        specified as [train_idx, class_prediction, prob_score, x1, y1, x2, y2]
        true_boxes (list): Similar as pred_boxes except all the correct ones 
        iou_threshold (float): threshold where predicted bboxes is correct
        box_format (str): "midpoint" or "corners" used to specify bboxes
        num_classes (int): number of classes
    Returns:
        float: mAP value across all classes given a specific IoU threshold 
    """

    # list storing all AP for respective classes
    average_precisions = []

    # used for numerical stability later on
    epsilon = 1e-16

    for c in range(num_classes):
        detections = []
        ground_truths = []

        # Go through all predictions and targets,
        # and only add the ones that belong to the
        # current class c
        for detection in pred_boxes:
            if detection[1] == c:
                detections.append(detection)

        for true_box in true_boxes:
            if true_box[1] == c:
                ground_truths.append(true_box)
#=================================        
                # find the amount of bboxes for each training example
        # Counter here finds how many ground truth bboxes we get
        # for each training example, so let's say img 0 has 3,
        # img 1 has 5 then we will obtain a dictionary with:
        # amount_bboxes = {0:3, 1:5}
        amount_bboxes = Counter([gt[0] for gt in ground_truths])

        # We then go through each key, val in this dictionary
        # and convert to the following (w.r.t same example):
        # ammount_bboxes = {0:torch.tensor[0,0,0], 1:torch.tensor[0,0,0,0,0]}
        for key, val in amount_bboxes.items():
            amount_bboxes[key] = torch.zeros(val)

        # sort by box probabilities which is index 2
        detections.sort(key=lambda x: x[2], reverse=True)
        # print("printing detections")
        # print(detections)
        # print(detections)
        # print(ground_truths)
        TP = torch.zeros((len(detections)))
        FP = torch.zeros((len(detections)))
        total_true_bboxes = len(ground_truths)
        
        # If none exists for this class then we can safely skip
        if total_true_bboxes == 0:
            continue

        for detection_idx, detection in enumerate(detections):
            # Only take out the ground_truths that have the same
            # training idx as detection
            ground_truth_img = [
                bbox for bbox in ground_truths if bbox[0] == detection[0]
            ]

            num_gts = len(ground_truth_img)
            best_iou = 0

            for idx, gt in enumerate(ground_truth_img):
                iou = box_iou(
                    torch.tensor(detection[3:]),
                    torch.tensor(gt[3:])
                )

                # print(iou)
                if iou > best_iou:
                    best_iou = iou
                    best_gt_idx = idx

            if best_iou > iou_threshold:
                # only detect ground truth detection once
                if amount_bboxes[detection[0]][best_gt_idx] == 0:
                    # true positive and add this bounding box to seen
                    TP[detection_idx] = 1
                    amount_bboxes[detection[0]][best_gt_idx] = 1
                else:
                    FP[detection_idx] = 1

            # if IOU is lower then the detection is a false positive
            else:
                FP[detection_idx] = 1

        TP_cumsum = torch.cumsum(TP, dim=0)
        FP_cumsum = torch.cumsum(FP, dim=0)
        recalls = TP_cumsum / (total_true_bboxes + epsilon)
        precisions = TP_cumsum / (TP_cumsum + FP_cumsum + epsilon)
        ap, mpre, mrec = compute_ap(list(recalls),list(precisions))
        precisions = torch.cat((torch.tensor([1]), precisions))
        # print(precisions)
        recalls = torch.cat((torch.tensor([0]), recalls))
        # print(recalls)
        # torch.trapz for numerical integration

    #     print(ap)
        average_precisions.append(ap)
        # average_precisions.append(torch.trapz(precisions, recalls))

    return sum(average_precisions) / len(average_precisions)

def metrics(json_path, split_class_path, target_path, safe_pred_path):
    with open(os.path.join(json_path, "best_predictions.json")) as json_file:
        data = json.load(json_file)
    df = pd.DataFrame(data)

    # class_df = pd.read_csv(split_class_path)


    true_boxes = []
    pred_boxes = []
    for target_txt in glob.glob(target_path):
        
        _,target_name = os.path.split(target_txt)
        name_only = os.path.splitext(target_name)[0]
        # print(name_only)
        image_df = df[df["image_id"]==name_only]
        
        for i,row in image_df.iterrows():
            pred_lis_for_sample = []
            pred_lis_for_sample.append(row["image_id"])
            pred_lis_for_sample.append(0)
            pred_lis_for_sample.append(row["score"])
            box = row["bbox"]
            xyxyBox = []
            xyxyBox.append(box[0])
            xyxyBox.append(box[1])
            xyxyBox.append(box[0] + box[2])
            xyxyBox.append(box[1] + box[3])
            pred_lis_for_sample.append(xyxyBox[0])
            pred_lis_for_sample.append(xyxyBox[1])
            pred_lis_for_sample.append(xyxyBox[2])
            pred_lis_for_sample.append(xyxyBox[3])
            pred_boxes.append(pred_lis_for_sample)
        with open (target_txt) as f:
            
            for cnt, line in enumerate(f):
                c,x,y,w,h = map(float, line.split())
                x = x*1024
                y = y*1024
                w = w*1024
                h = h*1024
                x1 = x - w/2
                x2 = x + w/2
                y1 = y - h/2
                y2 = y + h/2
                lis_for_each_sample = []
                lis_for_each_sample.append(name_only)
                lis_for_each_sample.append(0)
                lis_for_each_sample.append(1)
                lis_for_each_sample.append(x1)
                lis_for_each_sample.append(y1)
                lis_for_each_sample.append(x2)
                lis_for_each_sample.append(y2)
                
                true_boxes.append(lis_for_each_sample)
        # print(pred_boxes, true_boxes)
    for pred_txt in glob.glob(safe_pred_path):
        _,target_name = os.path.split(target_txt)
        name_only = os.path.splitext(target_name)[0]
        with open(pred_txt) as f:
            for line in f:
                c,x,y,w,h,cf = map(float, line.split())
                x = x*1024
                y = y*1024
                w = w*1024
                h = h*1024
                x1 = x - w/2
                x2 = x + w/2
                y1 = y - h/2
                y2 = y + h/2                
                pred_lis_for_sample = []
                pred_lis_for_sample.append(name_only)
                pred_lis_for_sample.append(0)
                pred_lis_for_sample.append(cf)
                pred_lis_for_sample.append(xyxyBox[0])
                pred_lis_for_sample.append(xyxyBox[1])
                pred_lis_for_sample.append(xyxyBox[2])
                pred_lis_for_sample.append(xyxyBox[3])
                pred_boxes.append(pred_lis_for_sample)
    iouvs = np.linspace(0.5,0.95,10)
    mAP = []
    for iouv in iouvs:
        ap = mean_average_precision(pred_boxes, true_boxes, iou_threshold=iouv)
        # print("ap{}: {}".format(iouv, ap))
        mAP.append(ap)
    # print("mAP: {}".format(sum(mAP)/len(mAP)))
    mAP.append(sum(mAP)/len(mAP))
    return mAP
"""
json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_hard1"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold1/labels/test_hard/*.txt" # only hard sample label files
split_class_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/split_class.csv"

mAP1 = metrics(json_path, split_class_path, target_path)
mAP1.append("fold1")
mAP1.append("hard")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_hard2"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold2/labels/test_hard/*.txt" # only hard sample label files

mAP2 = metrics(json_path, split_class_path, target_path)
mAP2.append("fold2")
mAP2.append("hard")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_hard3"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold3/labels/test_hard/*.txt" # only hard sample label files

mAP3 = metrics(json_path, split_class_path, target_path)
mAP3.append("fold3")
mAP3.append("hard")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_hard4"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold4/labels/test_hard/*.txt" # only hard sample label files

mAP4 = metrics(json_path, split_class_path, target_path)
mAP4.append("fold4")
mAP4.append("hard")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_hard5"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold5/labels/test_hard/*.txt" # only hard sample label files

mAP5 = metrics(json_path, split_class_path, target_path)
mAP5.append("fold5")
mAP5.append("hard")

mAP = []
mAP.append(mAP1)
mAP.append(mAP2)
mAP.append(mAP3)
mAP.append(mAP4)
mAP.append(mAP5)
#==========================
json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_easy1"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold1/labels/test_easy/*.txt" # only hard sample label files
split_class_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/split_class.csv"

mAP1 = metrics(json_path, split_class_path, target_path)
mAP1.append("fold1")
mAP1.append("easy")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_easy2"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold2/labels/test_easy/*.txt" # only hard sample label files

mAP2 = metrics(json_path, split_class_path, target_path)
mAP2.append("fold2")
mAP2.append("easy")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_easy3"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold3/labels/test_easy/*.txt" # only hard sample label files

mAP3 = metrics(json_path, split_class_path, target_path)
mAP3.append("fold3")
mAP3.append("easy")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_easy4"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold4/labels/test_easy/*.txt" # only hard sample label files

mAP4 = metrics(json_path, split_class_path, target_path)
mAP4.append("fold4")
mAP4.append("easy")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_easy5"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold5/labels/test_easy/*.txt" # only hard sample label files

mAP5 = metrics(json_path, split_class_path, target_path)
mAP5.append("fold5")
mAP5.append("easy")

mAP.append(mAP1)
mAP.append(mAP2)
mAP.append(mAP3)
mAP.append(mAP4)
mAP.append(mAP5)
"""
#====================
json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_1"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold1/labels/val/*.txt" # only hard sample label files
split_class_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/split_class.csv"
safe_pred_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/detect/safe_wardHistAdj_gamma_CC_001_1/labels/*.txt"

mAP1 = metrics(json_path, split_class_path, target_path, safe_pred_path)
mAP1.append("fold1")
mAP1.append("all")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_2"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold2/labels/val/*.txt" # only hard sample label files
safe_pred_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/detect/safe_wardHistAdj_gamma_CC_001_2/labels/*.txt"

mAP2 = metrics(json_path, split_class_path, target_path, safe_pred_path)
mAP2.append("fold2")
mAP2.append("all")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_3"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold3/labels/val/*.txt" # only hard sample label files
safe_pred_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/detect/safe_wardHistAdj_gamma_CC_001_3/labels/*.txt"

mAP3 = metrics(json_path, split_class_path, target_path, safe_pred_path)
mAP3.append("fold3")
mAP3.append("all")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_4"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold4/labels/val/*.txt" # only hard sample label files
safe_pred_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/detect/safe_wardHistAdj_gamma_CC_001_4/labels/*.txt"

mAP4 = metrics(json_path, split_class_path, target_path, safe_pred_path)
mAP4.append("fold4")
mAP4.append("all")

json_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_wardHistAdj_gamma_CC_2000/lc3_wardHistAdj_gamma_CC_2000_5"
target_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold5/labels/val/*.txt" # only hard sample label files
safe_pred_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/detect/safe_wardHistAdj_gamma_CC_001_5/labels/*.txt"

mAP5 = metrics(json_path, split_class_path, target_path, safe_pred_path)
mAP5.append("fold5")
mAP5.append("all")

mAP = []
mAP.append(mAP1)
mAP.append(mAP2)
mAP.append(mAP3)
mAP.append(mAP4)
mAP.append(mAP5)
#=============================

iouvs = list(np.linspace(0.5,0.95,10))
iouvs.append("mAP")
with open(os.path.join(Path(json_path).parent, "resultsWithSafeAP.csv"), mode='w') as ap_file:
    ap_writer = csv.writer(ap_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ap_writer.writerow(iouvs)
    ap_writer.writerows(mAP)
