import os
import glob
import matplotlib.pyplot as plt
from matplotlib import patches
import cv2
import json
import pandas as pd
import math

def gt_box(label_path):
    with open(label_path) as lines:
        gts = []
        for cnt, line in enumerate(lines):
            
            c,xp,yp,wp,hp = map(float, line.split())
            gt = []
            xp = xp*1024
            yp = yp*1024
            wp = wp*1024
            hp = hp*1024
            x = xp - wp/2
            y = 1024 - yp - hp/2
            gt.extend((x,y,wp,hp))
            gts.append(gt)
    return gts

def pred_box(df):
    
    all_pred = []
    for i, row in df.iterrows():
        
        row = row["bbox"]
        pred = []
        x = row[0]
        y = 1024 - row[1] - row[3]
        w = row[2]
        h = row[3]
        pred.extend((x,y,w,h))
        all_pred.append(pred)
    return all_pred
def subplot(axs, x,y,image,preds,gts):
    
    axs[x,y].axes.xaxis.set_visible(False)
    axs[x,y].axes.yaxis.set_visible(False)
    # axs.subplots_adjust(bottom=0.1, right=0.1, top=0, left=0)
    axs[x,y].imshow(image)

    for pred in preds:
        print(pred[0])
        print(pred[1])
        print(pred[2])
        print(pred[3])
        print(type(pred[0]))
        rect = patches.Rectangle((pred[0],pred[1]), pred[2], pred[3], edgecolor='r', facecolor='None')
        axs[x,y].add_patch(rect)

    for gt in gts:
        rect = patches.Rectangle((gt[0],gt[1]), gt[2], gt[3], edgecolor='g', facecolor='None')
        axs[x,y].add_patch(rect)
        

def visualize_results(label_path, img_path, results_path, conf_thres):
    with open(os.path.join(results_path, "best_predictions.json")) as json_file:
        results = json.load(json_file)
    results_df = pd.DataFrame(results)

    cnt = 0
    num_of_imgs = len(glob.glob(img_path))

    figure, axs = plt.subplots(2,2)

    for img in glob.glob(img_path):
        cnt+=1
        
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]
        image_df = results_df[(results_df["image_id"]==name_only) & (results_df["score"]>=conf_thres)]
        label_name = name_only + ".txt"
        if cnt%4 == 1:
            image = cv2.imread(img)
            preds = pred_box(image_df)
            gts = gt_box(os.path.join(label_path, label_name))
            subplot(axs, 0,0,image,preds,gts)    
        elif cnt%4 == 2:
            image = cv2.imread(img)
            preds = pred_box(image_df)
            gts = gt_box(os.path.join(label_path, label_name))
            subplot(axs, 0,1,image,preds,gts)
        elif cnt%4 == 3:
            image = cv2.imread(img)
            preds = pred_box(image_df)
            gts = gt_box(os.path.join(label_path, label_name))
            subplot(axs, 1,0,image,preds,gts)
        elif cnt%4 == 0:
            image = cv2.imread(img)
            preds = pred_box(image_df)
            gts = gt_box(os.path.join(label_path, label_name))
            subplot(axs, 1,1,image,preds,gts)
            figure.tight_layout()
            plt.savefig(os.path.join(results_path, "label_prediction{}_atConf{}".format(math.floor(cnt/4), conf_thres)+".png"))
            figure, axs = plt.subplots(2,2)
        if  cnt==num_of_imgs and cnt%4 != 0:
            plt.savefig(os.path.join(results_path, "label_prediction{}_atConf{}".format(math.ceil(cnt/4), conf_thres)))

if __name__=="__main__":
    label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/tonemap/reinhardLocal_gamma_CC/1024/lc3_reinhard_folds/fold1/labels/val"
    img_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/tonemap/reinhardLocal_gamma_CC/1024/lc3_reinhard_folds/fold1/images/val/*.png"
    results_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_30_2000_folds/lc3_30_2000_1"
    conf_thres = 0.25
    visualize_results(label_path, img_path, results_path, conf_thres)