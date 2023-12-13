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

def avgVarCal(image_path, label_path, df, csv_list):    
    label_names = sorted(os.listdir(label_path))

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
                img_crop = img[startY:endY,startX:endX]
                
                # mean, std = img_crop.mean(), img_crop.std()
                # img_crop = (img_crop-mean)/std
                
                avg = np.average(img_crop)
                variance = np.var(img_crop)
                
                lis = []
                lis.append(only_name)
                lis.append(image_num.group())
                lis.append(cnt+1)
                lis.append(i)
                lis.append(avg)
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
    return csv_list

image_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/big_small_dataset"
csv_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/split_class.csv"

df = pd.read_csv(csv_path)

title = ["img_name", "img_num", "split_num","sort_seq", "avg", "variance", "num_of_anno", "class_name"]
csv_list = []
image_small_path = os.path.join(image_path, "small/images")
image_big_path = os.path.join(image_path, "big/images")
label_small_path = os.path.join(image_path, "small/labels")
label_big_path = os.path.join(image_path, "big/labels")
csv_list = avgVarCal(image_small_path, label_small_path, df, csv_list)
csv_list = avgVarCal(image_big_path, label_big_path, df, csv_list)
# csv_list.sort(key=lambda x: x[4])
csv_list.insert(0,title)

with open("lc4_small_variance.csv", mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for max_lis in csv_list:
        csv_writer.writerow(max_lis)




    
