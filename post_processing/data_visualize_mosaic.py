import os
import glob
import matplotlib.pyplot as plt
from matplotlib import patches
import cv2
import json
import pandas as pd
import math
import numpy as np
from PIL import Image

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
            x1 = xp - wp/2
            y1 = yp - hp/2
            x2 = xp + wp/2
            y2 = yp + hp/2
            gt.extend((x1,y1,x2,y2))
            gts.append(gt)
    return gts

def pred_box(df):
    
    all_pred = []
    for i, row in df.iterrows():
        
        box = row["bbox"]
        conf = row["score"]
        pred = []
        x1 = box[0]
        y1 = box[1]
        x2 = box[0] + box[2]
        y2 = box[1] + box[3]
        pred.extend((x1, y1, x2, y2, conf))
        all_pred.append(pred)
    return all_pred
def plot_images(x,y,image,preds,gts):
    

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
        

def visualize_results(label_path, img_path, results_path, conf_thres, img_size, bs):
    with open(os.path.join(results_path, "best_predictions.json")) as json_file:
        results = json.load(json_file)
    results_df = pd.DataFrame(results)

    cnt = 0
    num_of_imgs = len(glob.glob(img_path))


    tl = 3
    tf = 2
    w=img_size[0]
    h=img_size[1]

    mosaic = np.full((int(bs*h/2), int(bs*w/2),3), 255, dtype=np.uint8)
    save_num = 0
    for img in glob.glob(img_path):
        
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]
        image_df = results_df[(results_df["image_id"]==name_only) & (results_df["score"]>=conf_thres)]
        label_name = name_only + ".txt"

        if cnt%bs<bs/2:
            block_x = int(w * (cnt%bs))
            block_y = 0
        else:
            block_x = int(w * (cnt%bs-bs/2))
            block_y = h

        image = cv2.imread(img)        
        preds = pred_box(image_df)
        gts = gt_box(os.path.join(label_path, label_name))

        # add image
        mosaic[block_y:block_y+h, block_x:block_x+w, :] = image
        cv2.putText(mosaic, name_only, (block_x + 10, block_y + 50), 0, tl / 3, [220, 220, 220], thickness=tf,
                        lineType=cv2.LINE_AA)
        #add gts
        for gt in gts:
            c1, c2 = (int(block_x + gt[0]), int(block_y + gt[1])), (int(block_x + gt[2]), int(block_y + gt[3]))
            cv2.rectangle(mosaic, c1, c2, (0, 255, 0), thickness=tl)
        for pred in preds:
            c1, c2 = (int(block_x + pred[0]), int(block_y + pred[1])), (int(block_x + pred[2]), int(block_y + pred[3]))
            cv2.rectangle(mosaic, c1, c2, (0, 0, 255), thickness=tl)
            cv2.putText(mosaic, str(round(pred[4], 2)), (c2[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        cnt+=1
        
        if cnt%bs==0:
            save_num+=1
            if not os.path.exists(os.path.join(results_path, "label_pred_plots")):
                os.makedirs(os.path.join(results_path, "label_pred_plots"))
            Image.fromarray(mosaic).save(os.path.join(results_path, "label_pred_plots", "label_prediction{}_conf{}".format(save_num, conf_thres)+".png"))
            mosaic = np.full((int(bs*h/2), int(bs*w/2),3), 255, dtype=np.uint8)
        elif cnt>=len(glob.glob(img_path)):
            save_num+=1
            Image.fromarray(mosaic).save("label_prediction{}_conf{}".format(save_num, conf_thres))
            
if __name__=="__main__":
    label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds/fold5/labels/val"
    img_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/tonemap/reinhardLocal_gamma_CC/1024/lc3_reinhard_folds/fold5/images/val/*.png"
    # img_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/tonemap/wardHistAdj_gamma_CC/1024/lc3_wardHistAdj_gamma_CC_folds/fold5/images/val/*.png"
    results_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/lc3/test/lc3_reinhard_2000_folds/lc3_reinhard_2000_5"
    conf_thres = 0.25
    visualize_results(label_path, img_path, results_path, conf_thres, (1024, 1024), 4)