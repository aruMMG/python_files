import os
import numpy as np
import cv2
import math
import statistics
import re
import csv
from operator import itemgetter
from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas as pd

image_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/split_rotate/images"
label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/60/1024/split_rotate/labels"
csv_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/split_class.csv"

df = pd.read_csv(csv_path)

label_names = sorted(os.listdir(label_path))
title = ["img_name", "img_num", "split_num","sort_seq", "variance", "num_of_anno", "class_name"]
csv_list = []
i=1
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

            startX = int(x-w/2)
            endX = int(x+w/2)
            startY = int(y-h/2)
            endY = int(y+h/2)
            # img_crop = img[startY:endY,startX:endX]
            
            # mean, std = img_crop.mean(), img_crop.std()
            # img_crop = (img_crop-mean)/std
            
            # avg = np.average(img_crop)
            variance = np.var(img)
            
            lis = []
            lis.append(only_name)
            lis.append(image_num.group())
            lis.append(cnt+1)
            lis.append(i)
            # lis.append(avg)
            lis.append(variance)
            data = df.loc[(df["img_name"] == only_name) & (df["split_num"]==(cnt+1))]
            class_name = data.class_name
            num_of_anno = data.num_of_anno
            class_name = pd.Series.tolist(class_name)
            num_of_anno = pd.Series.tolist(num_of_anno)
            assert (len(class_name)==1), "class_name ambigious for image name {}, split number {}".format(only_name, cnt+1) 
            assert (len(num_of_anno)==1), "num_of_anno ambigious for image name {}, split number {}".format(only_name, cnt+1) 
            lis.append(num_of_anno[0])
            lis.append(class_name[0])
            csv_list.append(lis)
            i+=1
csv_list.sort(key=lambda x: x[4])
csv_list.insert(0,title)

with open("full_image_split_only_variance.csv", mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for max_lis in csv_list:
        csv_writer.writerow(max_lis)




    
