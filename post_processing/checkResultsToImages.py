import os
import glob
from matplotlib.pyplot import plot_date

def makeResultsList(fileName):
    all_pred = []
    if os.path.isfile(fileName):
        with open(fileName) as lines:
            for line in lines:
                c,xp,yp,wp,hp,cf = map(float, line.split())
                pred = []
                xp = xp*1024
                yp = yp*1024
                wp = wp*1024
                hp = hp*1024
                x1 = xp - wp/2
                y1 = yp - hp/2
                x2 = xp + wp/2
                y2 = yp + hp/2
                pred.extend((x1,y1,x2,y2))
                all_pred.append(pred)
        return all_pred
    return False
def gtList(fileName, splitNum):
    gt = []
    with open(fileName) as lines:
        for i, line in enumerate(lines):
            if splitNum==i+1:
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
                return gt

def checkCorrect(preds, gt):

    def box_area(box):
        # box = 4xn
        return (box[2] - box[0]) * (box[3] - box[1])
    
    for pred in preds:
        area1 = box_area(gt)
        area2 = box_area(pred)
        dx = min(gt[0], pred[0]) - max(gt[2],pred[2])
        dy = min(gt[1],pred[1]) - max(gt[3],pred[3])
        inter = dx*dy
        iou = inter/(area1+area2-inter)
        if iou >=0.45:
            return True
import pandas as pd

if __name__=="__main__":
    detect_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/hdr/detect/hdr_hsv/test_all"
    label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold/lc3_30_folds"
    file = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/split_class.csv"
    fold_name = "test_all_lc3_hdr_hsv_25_"
    csv_df = pd.read_csv(file)
    for index, row in csv_df.iterrows():
        imageName = str(row["img_name"])
        split_num = row["split_num"]
        fileName = imageName + ".txt"
        if os.path.isfile(os.path.join(label_path, "fold1/labels/test_all", fileName)):
            lab_file_name = os.path.join(label_path, "fold1/labels/test_all", fileName)
            pred_file_name = os.path.join(detect_path, fold_name+"1", "labels", fileName)
            gt = gtList(lab_file_name, split_num)
            if not gt:
                continue
            preds = makeResultsList(pred_file_name)
        elif os.path.isfile(os.path.join(label_path, "fold2/labels/test_all", fileName)):
            lab_file_name = os.path.join(label_path, "fold2/labels/test_all", fileName)
            pred_file_name = os.path.join(detect_path, fold_name+"2", "labels", fileName)
            gt = gtList(lab_file_name, split_num)
            if not gt:
                continue
            preds = makeResultsList(pred_file_name)
        elif os.path.isfile(os.path.join(label_path, "fold3/labels/test_all", fileName)):
            lab_file_name = os.path.join(label_path, "fold3/labels/test_all", fileName)
            pred_file_name = os.path.join(detect_path, fold_name+"3", "labels", fileName)
            gt = gtList(lab_file_name, split_num)
            if not gt:
                continue
            preds = makeResultsList(pred_file_name)
        elif os.path.isfile(os.path.join(label_path, "fold4/labels/test_all", fileName)):
            lab_file_name = os.path.join(label_path, "fold4/labels/test_all", fileName)
            pred_file_name = os.path.join(detect_path, fold_name+"4", "labels", fileName)
            gt = gtList(lab_file_name, split_num)
            if not gt:
                continue
            preds = makeResultsList(pred_file_name)
        elif os.path.isfile(os.path.join(label_path, "fold5/labels/test_all", fileName)):
            lab_file_name = os.path.join(label_path, "fold5/labels/test_all", fileName)
            pred_file_name = os.path.join(detect_path, fold_name+"5", "labels", fileName)
            gt = gtList(lab_file_name, split_num)
            if not gt:
                continue
            preds = makeResultsList(pred_file_name)
        else:
            print("file not found for image: {}".format(imageName))
            continue

        ispred = False
        if preds:
            ispred = checkCorrect(preds, gt)
        if ispred:
            csv_df.at[index, "isPredHdrHsv"] = 1
        else:
            csv_df.at[index, "isPredHdrHsv"] = 0
    csv_df.to_csv(file, index=False)