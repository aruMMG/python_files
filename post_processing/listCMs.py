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
def calculateCM(pred_file_path, labels=np.array([])):
    confusion_matrix = ConfusionMatrix(nc=1,conf=0.20)                
    if Path(pred_file_path).is_file():
        preds = pred_box(pred_file_path)
        confusion_matrix.process_batch(detections=preds, labels=labels)
    else:
        confusion_matrix.process_batch(labels=labels)
    return confusion_matrix.matrix

def createList(matrix, each_image, labels, name_only, length):
    i=0
    while i<matrix[0,0]:
        each_image[i+length].append("split")
        i+=1
    j=0
    while j<matrix[1,0]:
        each_image[i+j+length].append("background")
        j+=1
    assert((i+j)==labels.shape[0]), "gt splits in confusion matrix is not equal to than the number of splits in sample"
    
    k=0
    while k<matrix[0,1]:
        if len(each_image)<=(i+j+k+length):
            each_image.append([name_only])
            p=2
            while p<len(each_image[-2]):
                each_image[-1].append("background")
                p+=1
        each_image[i+j+k+length].append("split")
        k+=1

    return each_image

def resultImageWise(path_labels, pred_path, safe_pred_path):
    each_image = []

    for target_txt in glob.glob(path_labels):
        
        _,target_name = os.path.split(target_txt)
        name_only = os.path.splitext(target_name)[0]
        labels = txt2labelarray(target_txt)
        prev_len = len(each_image)
        for i in range(labels.shape[0]):
            each_label = []
            each_label.extend([name_only, "split"])
            each_image.append(each_label)        # print(name_only)
        models = ["best_exp", "hdr", "reinhard", "wardHistAdj", "3_images"]
        for model in models:
            if model == "best_exp":
                pred_file_path = os.path.join(pred_path,model,"test/lc4_30_1/labels", target_name)
                matrix = calculateCM(pred_file_path, labels)
                each_image = createList(matrix, each_image, labels, name_only, prev_len)
            elif model == "hdr":
                pred_file_path = os.path.join(pred_path,model,"test/lc4_hdr_1/labels", target_name)
                matrix = calculateCM(pred_file_path, labels)
                each_image = createList(matrix, each_image, labels, name_only, prev_len)
            elif model == "reinhard":
                pred_file_path = os.path.join(pred_path,model,"test/lc4_reinhard_1/labels", target_name)
                matrix = calculateCM(pred_file_path, labels)
                each_image = createList(matrix, each_image, labels, name_only, prev_len)
            elif model == "wardHistAdj":
                pred_file_path = os.path.join(pred_path,model,"test/lc4_wardHistAdj_1/labels", target_name)
                matrix = calculateCM(pred_file_path, labels)
                each_image = createList(matrix, each_image, labels, name_only, prev_len)
            elif model == "3_images":
                pred_file_path = os.path.join(pred_path,model,"test/lc4_3_images_1/labels", target_name)
                matrix = calculateCM(pred_file_path, labels)
                each_image = createList(matrix, each_image, labels, name_only, prev_len)
                while len(each_image[-1])<7:
                    each_image[-1].append("background")
    return each_image
    #     # confusion_matrix.plot(save_dir=save_dir, names=["splits"])
    # for safe_pred in glob.glob(safe_pred_path):
    #     _,image_name = os.path.split(safe_pred)
    #     name_only = os.path.splitext(image_name)[0]
    #     each_label = [name_only, "background"]

if __name__=="__main__":
    path_labels = "/home/aru/phd/hdr/may19/yolov5/dataset/lc4_reinhard_folds/fold1/labels/val/*.txt"
    pred_path = "/home/aru/phd/hdr/results"
    safe_pred_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/results/hdr/detect/safe_lc4_hdr_001_1/labels/*.txt"
    result = resultImageWise(path_labels, pred_path, safe_pred_path)

    # sorted(cms1, key=lambda x: x[0])
    # sorted(safecms1, key=lambda x: x[0])
    # for i in range(14):
    #     cms1[i].append(safecms1[i][1])
    
    # sorted(cms5, key=lambda x: x[0])
    # sorted(safecms5, key=lambda x: x[0])
    # for i in range(14):
    #     cms5[i].append(safecms5[i][1])
    # for i in range(14):
    #     cms1[i].extend(cms2[i][1:])
    #     cms1[i].extend(cms3[i][1:])
    #     cms1[i].extend(cms4[i][1:])
    #     cms1[i].extend(cms5[i][1:])
    #     csvList.append(cms1[i])

    heading = ["name", "ground_truth", "best_exposure", "hdr", "reinhard", "wardHistAdj", "3_images"]
    if len(heading)==len(result[1]):
        with open(os.path.join(pred_path, "imageWise.csv"), mode='w') as ap_file:
            ap_writer = csv.writer(ap_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ap_writer.writerow(heading)
            ap_writer.writerows(result)