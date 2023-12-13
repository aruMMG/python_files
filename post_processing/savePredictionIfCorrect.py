import pandas as pd
import cv2
import os
import glob
import json
import math
import torch
from collections import Counter
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
def check_prediction(pred_boxes, true_boxes, iou_threshold=0.5):
    save_detection = []
    for detection_idx, detection in enumerate(pred_boxes):
        for idx, gt in enumerate(true_boxes):
            iou = box_iou(
                torch.tensor(detection[3:]),
                torch.tensor(gt[3:])
            )
            if iou>iou_threshold:
                save_detection.append(detection)
    return save_detection

def create_correct_prediction(label_path, results_path, conf_thres, img_size):
    with open(os.path.join(results_path, "best_predictions.json")) as json_file:
        results = json.load(json_file)
    results_df = pd.DataFrame(results)

    save_ditection_dict = {}
    for target_txt in glob.glob(label_path):
        pred_boxes = []
        true_boxes = []
        _,target_name = os.path.split(target_txt)
        name_only = os.path.splitext(target_name)[0]
        # print(name_only)
        image_df = results_df[results_df["image_id"]==name_only]
        for i,row in image_df.iterrows():
            if row["score"]>=conf_thres:
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
            
        save_detection = check_prediction(pred_boxes, true_boxes, iou_threshold=0.5)
        print(pred_boxes)
        print("\n")
        print(true_boxes)
        print("\n")
        print("\n")
        print("\n")
        if not os.path.exists(os.path.join(results_path, "correct_prediction03")):
            os.mkdir(os.path.join(results_path, "correct_prediction03"))
        lines = []
        for detection in save_detection:
            res = []
            res.append(detection[1])
            res.extend(detection[3:])
            res.append(detection[2])
            res_string = " ".join(map(str, res))
            lines.append(res_string)
        with open(os.path.join(results_path, "correct_prediction03", target_name),"w") as g:
                g.writelines(lines)



if __name__=="__main__":
    conf_thres = 0.30
    label_path = "/home/aru/phd/objective1/hdr/reinhard/fold1/labels/val/*.txt"
    results_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_1"
    create_correct_prediction(label_path, results_path, conf_thres, (1024, 1024))
    label_path = "/home/aru/phd/objective1/hdr/reinhard/fold2/labels/val/*.txt"
    results_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_2"
    create_correct_prediction(label_path, results_path, conf_thres, (1024, 1024))
    label_path = "/home/aru/phd/objective1/hdr/reinhard/fold3/labels/val/*.txt"
    results_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_3"
    create_correct_prediction(label_path, results_path, conf_thres, (1024, 1024))
    label_path = "/home/aru/phd/objective1/hdr/reinhard/fold4/labels/val/*.txt"
    results_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_4"
    create_correct_prediction(label_path, results_path, conf_thres, (1024, 1024))
    label_path = "/home/aru/phd/objective1/hdr/reinhard/fold5/labels/val/*.txt"
    results_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_5"
    create_correct_prediction(label_path, results_path, conf_thres, (1024, 1024))
