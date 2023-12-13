big_l, small_l, mix_l = [],[],{}
import os
import glob
import pandas as pd
import torch

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
def main(big_l, small_l, small_df, pred_path, gt_path):
    big, small = 0, 0
    for res in glob.glob(pred_path):
        res_name = os.path.basename(res).split(".")[0]
        if res_name in big_l:
            with open(res) as f:
                lines = f.readlines()
            if len(lines):
                big+=1
            else:
                print("No correct labels for : {}".format(res_name))
        elif res_name in small_l:
            with open(res) as f:
                lines = f.readlines()
            if len(lines):
                small+=1
            else:
                print("No correct labels for : {}".format(res_name))
        else:
            with open(res) as f:
                lines = f.readlines()
            assert len(lines)==1, "more than one line"
            line_l = lines[0].split()
            assert len(line_l)<=11, "more than two correct prediction"
            if len(line_l)>6:
                small+=1
                big+=1
            else:
                with open(os.path.join(gt_path, res_name+".txt")) as g:
                    true_lines = g.readlines()
                    count = 0
                    for true_line in true_lines:
                        count+=1    
                        c,x,y,w,h = map(float, true_line.split())
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
                        detection = list(map(float, line_l))
                        iou = box_iou(torch.tensor(detection[1:]), torch.tensor(lis_for_each_sample))
                        small_crack_num = small_df.loc[small_df["img_name"]==res_name, "split_num"].iloc[0]
                        if iou.item()>0.5 and count==small_crack_num:
                            small+=1
                        elif iou.item()>0.5:
                            big+=1
    return big, small
if __name__=="__main__":
    for p in glob.glob("/home/aru/phd/objective1/hdr/dataset/lc4/big/images/*.jpg"):
        name  = os.path.basename(p).split(".")[0]
        big_l.append(name)

    with open("/home/aru/phd/objective1/hdr/small.csv") as f:
        lines = f.readlines()
        for line in lines:
            name = line.split(",")[0]
            small_l.append(name)

    both_df = pd.read_csv("/home/aru/phd/objective1/hdr/both.csv")
    small_df = both_df[both_df["class_name"]=="small"]

    pred_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_1/correct_prediction03/*.txt"
    gt_path = "/home/aru/phd/objective1/hdr/reinhard/fold1/labels/val"
    print(main(big_l, small_l, small_df, pred_path, gt_path))

    pred_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_2/correct_prediction03/*.txt"
    gt_path = "/home/aru/phd/objective1/hdr/reinhard/fold2/labels/val"
    print(main(big_l, small_l, small_df, pred_path, gt_path))

    pred_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_3/correct_prediction03/*.txt"
    gt_path = "/home/aru/phd/objective1/hdr/reinhard/fold3/labels/val"
    print(main(big_l, small_l, small_df, pred_path, gt_path))

    pred_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_4/correct_prediction03/*.txt"
    gt_path = "/home/aru/phd/objective1/hdr/reinhard/fold4/labels/val"
    print(main(big_l, small_l, small_df, pred_path, gt_path))

    pred_path = "/home/aru/phd/objective1/hdr/dataset/lc4/results/hdr/test/lc4_hdr_5/correct_prediction03/*.txt"
    gt_path = "/home/aru/phd/objective1/hdr/reinhard/fold5/labels/val"
    print(main(big_l, small_l, small_df, pred_path, gt_path))