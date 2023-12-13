from itertools import count
import numpy as np
import glob
import os
import json
import pandas as pd
import csv

from utils import box_iou
def yolo_gt2x1y1x2y2(gt, pred=False):
    if not pred:
        c,x,y,w,h = map(float, gt.split())
    else:
        c,x,y,w,h = gt
    x = x*1024
    y = y*1024
    w = w*1024
    h = h*1024
    x1 = x - w/2
    x2 = x + w/2
    y1 = y - h/2
    y2 = y + h/2
    lis_for_each_sample = []
    lis_for_each_sample.append(x1)
    lis_for_each_sample.append(y1)
    lis_for_each_sample.append(x2)
    lis_for_each_sample.append(y2)

    return lis_for_each_sample  

def xywh2xyxy(box):
    xyxyBox = []
    xyxyBox.append(box[0])
    xyxyBox.append(box[1])
    xyxyBox.append(box[0] + box[2])
    xyxyBox.append(box[1] + box[3])
    return xyxyBox

def check_iou(gt, img_pred, iou_threshold=0.5):
    iou_prev = 0
    idx_to_remove = 100

    if not img_pred:
        return img_pred, iou_prev
    for pred_idx, pred in enumerate(img_pred):
        # xyxy_pred = xywh2xyxy(pred)
        iou = box_iou(gt, pred)
        if iou>iou_threshold and iou>iou_prev:
            iou_prev = iou
            idx_to_remove = pred_idx
    if idx_to_remove!=100:
        img_pred.pop(idx_to_remove)
    
    return img_pred, iou_prev



def res_indivisual(gt_path, prediction_paths, save_path, iou_threshold=0.5, conf_threshold=0.2):
    
    csv_list = [["image_id", "defect_idx", "iou", "res"]]

    df = []
    if os.path.isfile(prediction_paths[0]):
        
        for prediction_path in prediction_paths:
            with open(prediction_path) as json_file:
                data = json.load(json_file)
            df2 = pd.DataFrame(data)
            df.append(df2)
        df = pd.concat(df)
        threshold_df = df[df["score"]>=conf_threshold]

    for gt_file in glob.glob(gt_path):
        file_name = os.path.basename(gt_file).split(".")[0]

        img_pred = []
        if os.path.isdir(prediction_paths[0]):

            for prediction_path in prediction_paths:
                label_name = os.path.join(prediction_path, file_name + ".txt")
                if os.path.exists(label_name):        
                    with open(label_name, "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            l = [float(x) for x in line.split(" ")]
                            if l[5]>conf_threshold:
                                pred = yolo_gt2x1y1x2y2(l[:5], pred=True)
                                img_pred.append(pred)

        elif os.path.isfile(prediction_path):
            img_pred = threshold_df[threshold_df["image_id"]==file_name]["bbox"]
            img_pred = img_pred.tolist()
        
        else:
            print("prediction file not exist")

        list_each_img = [file_name]
        with open(gt_file, "r") as f:
            gts = f.readlines()
            for gt_idx, gt in enumerate(gts):
                list_each_img.append(gt_idx)
                gt = yolo_gt2x1y1x2y2(gt)
                img_pred, iou = check_iou(gt, img_pred, iou_threshold)
                res = 0
                if iou>iou_threshold:
                    res = 1
                csv_list.append([file_name, gt_idx, iou, res])
    with open(save_path, "w") as f:
        wr = csv.writer(f)
        wr.writerows(csv_list)

def res_indivisual_FP(prediction_paths, save_path, conf_threshold=0.2, safe=False, res_file=""):

    if safe:
        csv_list = [["image_id", "defect_idx", "res"]]
        for prediction_path in prediction_paths:
            assert os.path.isdir(prediction_path), "for safe image prediction path is not a direcory"
            prediction_path_glob = os.path.join(prediction_path, "*.txt")
            for pred in glob.glob(prediction_path_glob):
                img_name = os.path.basename(pred).split(".")[0]
                img_pred = []
                num = 0
                with open(pred, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        l = [float(x) for x in line.split(" ")]
                        if l[5]>conf_threshold:
                            csv_list.append([img_name, num, 1])
                            num+=1
                if num==0:
                    csv_list.append([img_name, 0,0])

        with open(save_path, "w") as f:
            wr = csv.writer(f)
            wr.writerows(csv_list)
    else:
        csv_list = [["image_id", "defect_idx", "res"]]

        df = pd.read_csv(res_file)


        for prediction_path in prediction_paths:
            num=0
            assert os.path.isdir(prediction_path), "for safe image prediction path is not a direcory"
            prediction_path_glob = os.path.join(prediction_path, "*.txt")
       
            for pred in glob.glob(prediction_path_glob):
                img_name = os.path.basename(pred).split(".")[0]
                num = 0
                num_cor_pred = len(df[df["image_id"]==img_name])
                with open(pred, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        l = [float(x) for x in line.split(" ")]
                        if l[5]>conf_threshold:
                            num+=1

                if num<=num_cor_pred:
                    csv_list.append([img_name, 0,0])
                else:
                    for n in range(num-num_cor_pred):
                        csv_list.append([img_name, n,1])

        with open(save_path, "w") as f:
            wr = csv.writer(f)
            wr.writerows(csv_list)

if __name__=="__main__":
    # gt_paths = "/home/sakuni/phd/results/all_labels/*.txt"
    # prediction_paths = ["/home/sakuni/phd/results/best_exp/test/lc4_30_1/labels",
    #                     "/home/sakuni/phd/results/best_exp/test/lc4_30_2/labels",
    #                     "/home/sakuni/phd/results/best_exp/test/lc4_30_3/labels",
    #                     "/home/sakuni/phd/results/best_exp/test/lc4_30_4/labels",
    #                     "/home/sakuni/phd/results/best_exp/test/lc4_30_5/labels"
    #                     ]
    # save_path = "/home/sakuni/phd/results/best_exp/res_indivisual_04.csv"
    # res_indivisual(gt_paths, prediction_paths, save_path, conf_threshold=0.4)

    res_file = "/home/sakuni/phd/results/3_images/res_indivisual.csv"
    prediction_paths = ["/home/sakuni/phd/results/3_images/detect/safe_lc4_3_images_001_1/labels",
                        "/home/sakuni/phd/results/3_images/detect/safe_lc4_3_images_001_2/labels",
                        "/home/sakuni/phd/results/3_images/detect/safe_lc4_3_images_001_3/labels",
                        "/home/sakuni/phd/results/3_images/detect/safe_lc4_3_images_001_4/labels",
                        "/home/sakuni/phd/results/3_images/detect/safe_lc4_3_images_001_5/labels",
                        ]
    save_path = "/home/sakuni/phd/results/3_images/res_indivisual_FP_safe.csv"
    res_indivisual_FP(prediction_paths, save_path, conf_threshold=0.2, safe=True)