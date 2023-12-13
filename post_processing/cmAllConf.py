"""
Two function to plot confusion matrix.
mainOnly takes labels_path (/*.txt), pred_path(directory contain prediction for each images in txt format), save path.
    save confusionMatrix.png to save path.

mainSafe takes labels_path (/*.txt), pred_path(directory contain prediction for each images in txt format), safe_pred_path
(path with /*.txt, prediction for safe (no annotation) images), save path.
    save confusionMatrixSafeInclude.png to save path.
mainOnly calls class ConfusionMatrix internally to plot.
Other functions used are box_iou: calculate iou between two tensors. each tensor can have multiple box.

function txt2labelArray take txt file and return array of boxes.
fun pred_box take pred_path and return array of prediction

label_path txt file format: cl, x, y, w, h
pred_path txt file format: cl, x, y, w, h, conf
safe_pred_path txt file format: same as pred_path
"""


import numpy as np
import torch
import matplotlib.pyplot as plt
import csv


def box_iou(box1, box2):
    # https://github.com/pytorch/vision/blob/master/torchvision/ops/boxes.py
    """
    Return intersection-over-union (Jaccard index) of boxes.
    Both sets of boxes are expected to be in (x1, y1, x2, y2) format.
    Arguments:
        box1 (Tensor[N, 4])
        box2 (Tensor[M, 4])
    Returns:
        iou (Tensor[N, M]): the NxM matrix containing the pairwise
            IoU values for every element in boxes1 and boxes2
    """

    def box_area(box):
        # box = 4xn
        return (box[2] - box[0]) * (box[3] - box[1])

    area1 = box_area(box1.T)
    area2 = box_area(box2.T)

    # inter(N,M) = (rb(N,M,2) - lt(N,M,2)).clamp(0).prod(2)
    inter = (torch.min(box1[:, None, 2:], box2[:, 2:]) - torch.max(box1[:, None, :2], box2[:, :2])).clamp(0).prod(2)
    return inter / (area1[:, None] + area2 - inter)  # iou = inter / (area1 + area2 - inter)

class ConfusionMatrix:
    # Updated version of https://github.com/kaanakan/object_detection_confusion_matrix
    def __init__(self, nc, conf=0.75, iou_thres=0.50):
        self.matrix = np.zeros((nc + 1, nc + 1))
        self.nc = nc  # number of classes
        self.conf = conf
        self.iou_thres = iou_thres
        self.detection_counter = 0
        self.gt_counter = 0
    def process_batch(self, detections=np.array([]), labels=np.array([])):
        """
        Return intersection-over-union (Jaccard index) of boxes.
        Both sets of boxes are expected to be in (x1, y1, x2, y2) format.
        Arguments:
            detections (Array[N, 6]), x1, y1, x2, y2, conf, class
            labels (Array[M, 5]), class, x1, y1, x2, y2
        Returns:
            None, updates confusion matrix accordingly
        """
        # print(labels.shape)
        count=0
        if labels.size==0 and detections.size==0:
            pass
        elif labels.size==0:
            detections = detections[detections[:, 4] > self.conf]
            detection_classes = detections[:, 5].real.astype(int)
            self.detection_counter += detections.shape[0]
        
            for i, dc in enumerate(detection_classes):
                # print("0,1")
                self.matrix[dc, self.nc] += 1  # background FN
        elif detections.size==0:
            gt_classes = labels[:, 0].real.astype(int)
            self.gt_counter += labels.shape[0]
            for i, gc in enumerate(gt_classes):
                self.matrix[self.nc, gc] += 1
        else:
            detections = detections[detections[:, 4] > self.conf]
            detection_classes = detections[:, 5].real.astype(int)
            # print(detections.shape)
            self.detection_counter += detections.shape[0]
            self.gt_counter += labels.shape[0]
        
            gt_classes = labels[:, 0].real.astype(int)
            iou = box_iou(torch.Tensor(labels[:, 1:]), torch.Tensor(detections[:, :4]))
            # print(iou)
            x = torch.where(iou > self.iou_thres)
            # print(x)
            if x[0].shape[0]:
                matches = torch.cat((torch.stack(x, 1), iou[x[0], x[1]][:, None]), 1).cpu().numpy()
                if x[0].shape[0] > 1:
                    matches = matches[matches[:, 2].argsort()[::-1]]
                    matches = matches[np.unique(matches[:, 1], return_index=True)[1]]
                    matches = matches[matches[:, 2].argsort()[::-1]]
                    matches = matches[np.unique(matches[:, 0], return_index=True)[1]]
            else:
                matches = np.zeros((0, 3))
            # print(matches)
            n = matches.shape[0] > 0
            m0, m1, _ = matches.transpose().astype(np.int16)
            for i, gc in enumerate(gt_classes):
                j = m0 == i
                if n and sum(j) == 1:
                    self.matrix[detection_classes[m1[j]], gc] += 1  # correct
                    # print("0,0")
                elif n and not sum(j)==1:
                    # print("1,0")
                    self.matrix[self.nc, gc] += 1  # background FP
                else:
                    self.matrix[self.nc, gc] += 1  # background FP
                    # print("1,0")
                    count+=1
                    if count==1:
                        for i, dc in enumerate(detection_classes):
                            if not any(m1 == i):
                                # print("0,1")
                                self.matrix[dc, self.nc] += 1  # background FN

            if n:
                for i, dc in enumerate(detection_classes):
                    if not any(m1 == i):
                        # print("0,1")
                        self.matrix[dc, self.nc] += 1  # background FN
            # column_sum = self.matrix.sum(axis=0)
            # row_sum = self.matrix.sum(axis=1)
            # for i in range(nc+1):
        assert self.detection_counter == np.triu(self.matrix).sum() , "detection{} are same as matrx{}".format(self.detection_counter, np.triu(self.matrix).sum())
        assert self.gt_counter == np.tril(self.matrix).sum(), "gt are same as matrx"
    def matrix(self):
        return self.matrix

    def plot(self, save_dir='', names=(), safe=False):

        try:
            import seaborn as sn

            array = self.matrix # / (self.matrix.sum(0).reshape(1, self.nc + 1) + 1E-6)  # normalize

            array[array < 0.005] = np.nan  # don't annotate (would appear as 0.00)

            fig = plt.figure(figsize=(12, 9))
            sn.set(font_scale=1.0 if self.nc < 50 else 0.8)  # for label size
            labels = (0 < len(names) < 99) and len(names) == self.nc  # apply names to ticklabels

            sn.heatmap(array, annot=self.nc < 30, annot_kws={"size": 8}, cmap='Blues', fmt='.2f', square=True,
                       xticklabels=names + ['background'] if labels else "auto",
                       yticklabels=names + ['background'] if labels else "auto").set_facecolor((1, 1, 1))
            fig.axes[0].set_xlabel('True')
            fig.axes[0].set_ylabel('Predicted')
            fig.tight_layout()
            if safe:
                fig.savefig(Path(save_dir) / 'confusionMatrixSafeInclude'+str(self.conf)+'.png', dpi=250)
            else:
                fig.savefig(Path(save_dir) / 'confusionMatrix'+str(self.conf)+'.png', dpi=250)
        except Exception as e:
            pass

    def print(self):
        for i in range(self.nc + 1):
            print(' '.join(map(str, self.matrix[i])))


def txt2labelarray(txtFile):
    true_boxes = []

    with open(txtFile) as f:
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
            lis_for_each_sample.append(0)
            lis_for_each_sample.append(x1)
            lis_for_each_sample.append(y1)
            lis_for_each_sample.append(x2)
            lis_for_each_sample.append(y2)
            
            true_boxes.append(lis_for_each_sample)
        labels = np.asarray(true_boxes)
    return labels
def pred_box(pred_path):
    
    all_pred = []
    with open(pred_path) as lines:
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
            pred.extend((x1,y1,x2,y2,cf,c))
            all_pred.append(pred)
    return np.asarray(all_pred)
import glob
import os
from pathlib import Path

def mainOnly(path_labels, pred_path, save_dir, iou):
    cms = []
    confs = [0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75]
    for con in confs:
        cm = []
        confusion_matrix = ConfusionMatrix(nc=1,conf=con, iou_thres=iou)
        for target_txt in glob.glob(path_labels):
            
            _,target_name = os.path.split(target_txt)
            name_only = os.path.splitext(target_name)[0]
            labels = txt2labelarray(target_txt)
            # print(name_only)
            if Path(os.path.join(pred_path, target_name)).is_file():
                preds = pred_box(os.path.join(pred_path, target_name))
                confusion_matrix.process_batch(detections=preds, labels=labels)
            else:
                confusion_matrix.process_batch(labels=labels)
        cm.append(con)
        cm.append(confusion_matrix.matrix[0,0])
        cm.append(confusion_matrix.matrix[0,1])
        cm.append(confusion_matrix.matrix[1,0])
        cms.append(cm)
    return cms
        # confusion_matrix.plot(save_dir=save_dir, names=["splits"])
    # for safe_pred in glob.glob(safe_pred_path):
    #     preds = pred_box(safe_pred)
    #     confusion_matrix.process_batch(detections=preds)

    # confusion_matrix.plot(save_dir=save_dir, names=["splits"], safe=True)

def mainSafe(path_labels, pred_path, safe_pred_path, save_dir, iou):
    
    cms=[]
    confs = [0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75]
    for con in confs:
        cm = []
        confusion_matrix = ConfusionMatrix(nc=1,conf=con, iou_thres=iou)
        for target_txt in glob.glob(path_labels):
            
            _,target_name = os.path.split(target_txt)
            name_only = os.path.splitext(target_name)[0]
            labels = txt2labelarray(target_txt)
            # print(name_only)
            if Path(os.path.join(pred_path, target_name)).is_file():
                preds = pred_box(os.path.join(pred_path, target_name))
                confusion_matrix.process_batch(detections=preds, labels=labels)
            else:
                confusion_matrix.process_batch(labels=labels)

        # confusion_matrix.plot(save_dir=save_dir, names=["splits"])
        for safe_pred in glob.glob(safe_pred_path):
            preds = pred_box(safe_pred)
            confusion_matrix.process_batch(detections=preds)
        cm.append(con)
        cm.append(confusion_matrix.matrix[0,1])
        cms.append(cm)
    return cms   
        # confusion_matrix.plot(save_dir=save_dir, names=["splits"], safe=True)
if __name__=="__main__":
    ious = [0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
    for iou in ious:
        csvList = []
        path_labels = "/home/sakuni/phd/objective2/dataset/real_folds/fold1/labels/val/*.txt"
        pred_path = "/home/sakuni/phd/results/p2/test/all/10_real/10_real_80_synth/10_real_80_synth_fold1/labels"
        safe_pred_path = "/home/sakuni/phd/results/p2/test/detect/safe_10_real/synth_80/safe_10_real_80_synth_fold1/labels/*.txt"
        save_dir = "/home/sakuni/phd/results/p2/test/all/10_real/10_real_80_synth"
        cms1 = mainOnly(path_labels, pred_path, save_dir, iou)
        safecms1 = mainSafe(path_labels, pred_path, safe_pred_path, save_dir, iou)
        # print(cms1)
        # print(safecms1)
        sorted(cms1, key=lambda x: x[0])
        sorted(safecms1, key=lambda x: x[0])
        for i in range(14):
            cms1[i].append(safecms1[i][1])
        # print(cms1)
        path_labels = "/home/sakuni/phd/objective2/dataset/real_folds/fold2/labels/val/*.txt"
        pred_path = "/home/sakuni/phd/results/p2/test/all/10_real/10_real_80_synth/10_real_80_synth_fold2/labels"
        safe_pred_path = "/home/sakuni/phd/results/p2/test/detect/safe_10_real/synth_80/safe_10_real_80_synth_fold2/labels/*.txt"
        # save_dir = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/results/wardHistAdj/test/lc4_wardHistAdj_2"
        cms2 = mainOnly(path_labels, pred_path, save_dir, iou)
        safecms2 = mainSafe(path_labels, pred_path, safe_pred_path, save_dir, iou)
        sorted(cms2, key=lambda x: x[0])
        sorted(safecms2, key=lambda x: x[0])
        for i in range(14):
            cms2[i].append(safecms2[i][1])

        path_labels = "/home/sakuni/phd/objective2/dataset/real_folds/fold3/labels/val/*.txt"
        pred_path = "/home/sakuni/phd/results/p2/test/all/10_real/10_real_80_synth/10_real_80_synth_fold3/labels"
        safe_pred_path = "/home/sakuni/phd/results/p2/test/detect/safe_10_real/synth_80/safe_10_real_80_synth_fold3/labels/*.txt"
        # save_dir = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/results/wardHistAdj/test/lc4_wardHistAdj_3"
        cms3 = mainOnly(path_labels, pred_path, save_dir, iou)
        safecms3 = mainSafe(path_labels, pred_path, safe_pred_path, save_dir, iou)
        sorted(cms3, key=lambda x: x[0])
        sorted(safecms3, key=lambda x: x[0])
        for i in range(14):
            cms3[i].append(safecms3[i][1])

        path_labels = "/home/sakuni/phd/objective2/dataset/real_folds/fold4/labels/val/*.txt"
        pred_path = "/home/sakuni/phd/results/p2/test/all/10_real/10_real_80_synth/10_real_80_synth_fold4/labels"
        safe_pred_path = "/home/sakuni/phd/results/p2/test/detect/safe_10_real/synth_80/safe_10_real_80_synth_fold4/labels/*.txt"
        # save_dir = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/results/wardHistAdj/test/lc4_wardHistAdj_4"
        cms4 = mainOnly(path_labels, pred_path, save_dir, iou)
        safecms4 = mainSafe(path_labels, pred_path, safe_pred_path, save_dir, iou)
        sorted(cms4, key=lambda x: x[0])
        sorted(safecms4, key=lambda x: x[0])
        for i in range(14):
            cms4[i].append(safecms4[i][1])

        path_labels = "/home/sakuni/phd/objective2/dataset/real_folds/fold5/labels/val/*.txt"
        pred_path = "/home/sakuni/phd/results/p2/test/all/10_real/10_real_80_synth/10_real_80_synth_fold5/labels"
        safe_pred_path = "/home/sakuni/phd/results/p2/test/detect/safe_10_real/synth_80/safe_10_real_80_synth_fold5/labels/*.txt"
        # save_dir = "/home/sakuni/phd/results/p2/test/all/10_real/10_real"
        cms5 = mainOnly(path_labels, pred_path, save_dir, iou)
        safecms5 = mainSafe(path_labels, pred_path, safe_pred_path, save_dir, iou)
        sorted(cms5, key=lambda x: x[0])
        sorted(safecms5, key=lambda x: x[0])
        for i in range(14):
            cms5[i].append(safecms5[i][1])
        for i in range(14):
            cms1[i].extend(cms2[i][1:])
            cms1[i].extend(cms3[i][1:])
            cms1[i].extend(cms4[i][1:])
            cms1[i].extend(cms5[i][1:])
            csvList.append(cms1[i])

        heading = ["conf", "TP1", "FP1", "FN1", "FPS1", "TP2", "FP2", "FN2", "FPS2", "TP3", "FP3", "FN3", "FPS3", "TP4", "FP4", "FN4", "FPS4", "TP5", "FP5", "FN5", "FPS5"]
        if len(heading)==len(csvList[1]):
            with open(os.path.join(save_dir, "CM"+str(iou)+".csv"), mode='w') as ap_file:
                ap_writer = csv.writer(ap_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                ap_writer.writerow(heading)
                ap_writer.writerows(csvList)