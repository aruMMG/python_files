from genericpath import exists
import cv2
import os
def drawline(img,pt1,pt2,color,thickness=1,style='dotted',gap=20):
    dist =((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**.5
    pts= []
    for i in  np.arange(0,dist,gap):
        r=i/dist
        x=int((pt1[0]*(1-r)+pt2[0]*r)+.5)
        y=int((pt1[1]*(1-r)+pt2[1]*r)+.5)
        p = (x,y)
        pts.append(p)

    if style=='dotted':
        for p in pts:
            cv2.circle(img,p,thickness,color,-1)
    else:
        s=pts[0]
        e=pts[0]
        i=0
        for p in pts:
            s=e
            e=p
            if i%2==1:
                cv2.line(img,s,e,color,thickness)
            i+=1

def drawpoly(img,pts,color,thickness=1,style='dotted',):
    s=pts[0]
    e=pts[0]
    pts.append(pts.pop(0))
    for p in pts:
        s=e
        e=p
        drawline(img,s,e,color,thickness,style)

def drawrect(img,pt1,pt2,color,thickness=1,style='dotted'):
    pts = [pt1,(pt2[0],pt1[1]),pt2,(pt1[0],pt2[1])] 
    drawpoly(img,pts,color,thickness,style)

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

def pred_box_safe(pred_path, conf_thres):
    with open(pred_path) as lines:
        all_pred = []

        for cnt, line in enumerate(lines):
            c,xp,yp,wp,hp, conf = map(float, line.split())
            if conf < conf_thres:
                continue
            xp = xp*1024
            yp = yp*1024
            wp = wp*1024
            hp = hp*1024
            x1 = xp - wp/2
            y1 = yp - hp/2
            x2 = xp + wp/2
            y2 = yp + hp/2
            pred = []
            pred.extend((x1, y1, x2, y2, conf))
            all_pred.append(pred)
    return all_pred

        
import json
import pandas as pd
import glob
import numpy as np
import math
def visualize_results(label_path, img_path, results_path, conf_thres, img_size):
    with open(os.path.join(results_path, "best_predictions.json")) as json_file:
        results = json.load(json_file)
    results_df = pd.DataFrame(results)

    cnt = 0
    num_of_imgs = len(glob.glob(img_path))


    tl = 3
    tf = 2
    w=img_size[0]
    h=img_size[1]

    for img in glob.glob(img_path):
        
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]
        image_df = results_df[(results_df["image_id"]==name_only) & (results_df["score"]>=conf_thres)]
        label_name = name_only + ".txt"


        image = cv2.imread(img)        
        preds = pred_box(image_df)
        gts = gt_box(os.path.join(label_path, label_name))

        #add gts
        for gt in gts:
            c1, c2 = (math.floor(gt[0]),math.floor(gt[1])), (math.floor(gt[2]),math.floor(gt[3]))
            image = cv2.rectangle(image, c1, c2, (0, 255, 0), 3)
        for pred in preds:
            c1, c2 = (math.floor(pred[0]), math.floor(pred[1])), (math.floor(pred[2]), math.floor(pred[3]))
            image = cv2.rectangle(image, c1, c2, (255, 0, 0), tl)
            image = cv2.putText(image, str(round(pred[4], 2)), (c2[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        cv2.imwrite(os.path.join(results_path, "plots",name_only+".png"), image)

def visualize_results_safe(img_path, results_path, conf_thres, img_size):

    cnt = 0
    num_of_imgs = len(glob.glob(img_path))


    tl = 3
    tf = 2
    w=img_size[0]
    h=img_size[1]

    for img in glob.glob(img_path):
        
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]
        label_name = name_only + ".txt"


        image = cv2.imread(img)
        if exists(os.path.join(results_path, "labels", label_name)):
            preds = pred_box_safe(os.path.join(results_path, "labels", label_name), conf_thres)
        else:
            continue
        #add gts
        for pred in preds:
            c1, c2 = (math.floor(pred[0]), math.floor(pred[1])), (math.floor(pred[2]), math.floor(pred[3]))
            image = cv2.rectangle(image, c1, c2, (255, 0, 0), tl)
            image = cv2.putText(image, str(round(pred[4], 2)), (c2[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        cv2.imwrite(os.path.join(results_path, "images",name_only+".png"), image)



if __name__=="__main__":
    label_path = "/home/sakuni/datasets/Real_test/fold3/labels/val"
    img_path = "/home/sakuni/datasets/Real_test/60/fold3/*.jpg"
    # img_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/tonemap/wardHistAdj_gamma_CC/1024/lc3_wardHistAdj_gamma_CC_folds/fold5/images/val/*.png"
    results_path = "/home/sakuni/phd/results/p2/test/thanos/80_synth_140FullLarge_enlarge_label_folds/80_synth_140FullLarge_enlarge_label_001_fold3"
    conf_thres = 0.20
    visualize_results(label_path, img_path, results_path, conf_thres, (1024, 1024))
    img_path_safe = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/tonemap/wardHistAdj_gamma_CC/1024/safe/*.png"
    results_path_safe = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/results/wardHistAdj/detect/safe_lc4_wardHistAdj_001_5"
    # visualize_results_safe(img_path_safe, results_path_safe, conf_thres, (1024, 1024))