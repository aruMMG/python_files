import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

import cv2 as cv
import numpy as np


path = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/full/calibration/raw/11"
path_dst1 = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/full/calibration/raw/3exp1"
path_dst2 = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/full/calibration/raw/3exp2"


# Loading exposure images into a list

dirs = sorted(os.listdir(path))
i=0
in_list = []
final_list = []
for file in dirs:
    in_list.append(file)
    i+=1
    if (i%11==0):
        final_list.append(in_list)
        i=0
        in_list = []

j=113
for img_fn in final_list:
    #print(img_fn)
    #print(j)
    j+=1
    img_list = []
    exposure_times = []
    count15=0
    count30=0
    count60=0
    count125=0
    count250=0
    count500=0
    for img in img_fn:
        #print(img)

        exif = {}
        image = Image.open(os.path.join(path,img))
        for tag, value in image._getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]]=value
        
        if 'ExposureTime' in exif:
            extime=round(exif['ExposureTime'],6)

            if(abs(extime-0.06666666666667)<0.000001 and count15==0):
                shutil.copy2(os.path.join(path,img),path_dst2)
                count15+=1

            elif(abs(extime-0.03333333333333)<0.000001 and count30==0):
                shutil.copy2(os.path.join(path,img),path_dst1)
                count30+=1

            elif(abs(extime-0.0166666666666)<0.000001 and count60==0):
                shutil.copy2(os.path.join(path,img),path_dst2)
                count60+=1
             
            elif(abs(extime-0.008)<0.000001 and count125==0):
                shutil.copy2(os.path.join(path,img),path_dst1)   
                count125+=1
                
            elif(abs(extime-0.004)<0.000001 and count250==0):
                shutil.copy2(os.path.join(path,img),path_dst2)
                count250+=1

            elif(abs(extime-0.002)<0.000001 and count500==0):
                shutil.copy2(os.path.join(path,img),path_dst1)
                count500+=1
            else:
                continue