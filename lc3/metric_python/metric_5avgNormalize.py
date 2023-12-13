import os
import numpy as np
import cv2
import math
import statistics
import re
import csv

image_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/split/images"
label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/60/1024/split/labels"

label_names = sorted(os.listdir(label_path))
csv_list = []
for name in label_names:
    
    txt_path = os.path.join(label_path,name)
    only_name, ext = os.path.splitext(name)
    image_num = re.search(r"\d+", only_name)
    image_name = only_name+".jpg"
    image_path_name = os.path.join(image_path,image_name)

    img = cv2.cvtColor(cv2.imread(image_path_name), cv2.COLOR_BGR2XYZ)[:,:,1]
    with open(txt_path) as f:
        for cnt, line in enumerate(f):
            c,x,y,w,h = map(float, line.split())
            x = x*1024
            y = y*1024
            w = w*1024
            h = h*1024
            if h>w:
                startX = int(x-w/2-10)
                endX = int(x+w/2+10)
                startY = int(y-h/2)
                endY = int(y+h/2)
                kernel = np.array([[-1,-1,-1,-1,-1,1,1,1,1,1]])

            else:
                endX = int(x+w/2)
                startX = int(x-w/2)
                endY = int(y+h/2+10)
                startY = int(y-h/2-10)
                kernel = np.array([[-1],
                                    [-1],
                                    [-1],
                                    [-1],
                                    [-1],
                                    [1],
                                    [1],
                                    [1],
                                    [1],
                                    [1]])
            
            H = np.floor(np.array(kernel.shape)/2).astype(np.int)
            img_crop = img[startY:endY,startX:endX]
            maxi, mini = np.max(img_crop), np.min(img_crop)
            img_crop = img_crop/(maxi-mini)
            img_masked = np.abs(cv2.filter2D(img_crop, ddepth=-1, kernel=kernel))
            if h>w:
                img_masked = img_masked[:,H[1]:-H[1]+1]
                row_max = np.amax(img_masked,axis=1)
            else:
                img_masked = img_masked[H[0]:-H[0]+1,:]
                row_max = np.amax(img_masked,axis=0)
                
            difference = statistics.mean(row_max)

            max_lis = []
            max_lis.append(only_name)
            max_lis.append(image_num.group())
            max_lis.append(difference)
            csv_list.append(max_lis)

with open("5avgNormalized+10.csv", mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for max_lis in csv_list:
        csv_writer.writerow(max_lis)

    
