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
                anno_startX = int(x-w/2)
                anno_endX = int(x+w/2)
                endX = int(x+w/2+10)
                startY = int(y-h/2)
                endY = int(y+h/2)
                img_crop = img[startY:endY,startX:endX]
                
                maxi, mini = np.max(img_crop), np.min(img_crop)
                img_crop = img_crop/(maxi-mini)
                
                avg_big = np.average(img_crop)
                avg_small = np.average(img_crop[:,10:endX-10])
                num_big_pix = (endX-startX)*(endY-startY)
                num_small_pix = (anno_endX-anno_startX)*(endY-startY)


            else:
                endX = int(x+w/2)
                startX = int(x-w/2)
                anno_endY = int(x+h/2)
                anno_startY = int(x-h/2)
                endY = int(y+h/2+10)
                startY = int(y-h/2-10)
                img_crop = img[startY:endY,startX:endX]

                maxi, mini = np.max(img_crop), np.min(img_crop)
                img_crop = img_crop/(maxi-mini)

                avg_big = np.average(img_crop)
                avg_small = np.average(img_crop[10:endY-10,:])
                num_big_pix = (endX-startX)*(endY-startY)
                num_small_pix = (endX-startX)*(anno_endY-anno_startY)
            avg_out = (avg_big*num_big_pix-avg_small*num_small_pix)/(num_big_pix-num_small_pix)
            difference = np.abs(avg_small-avg_out)
            max_lis = []
            max_lis.append(only_name)
            max_lis.append(image_num.group())
            max_lis.append(difference)
            csv_list.append(max_lis)

with open("avgNormalized+10.csv", mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for max_lis in csv_list:
        csv_writer.writerow(max_lis)

    
