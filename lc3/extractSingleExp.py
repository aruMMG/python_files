import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

import cv2 as cv
import numpy as np


path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/new_crack"
path_dst4 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/4000/split"
path_dst4_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/4000/split_rotate"
path_dst8 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/2000/split"
path_dst8_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/2000/split_rotate"
path_dst15 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/15/split"
path_dst15_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/15/split_rotate"
path_dst30 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/split"
path_dst30_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/split_rotate"
path_dst60 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/60/split"
path_dst60_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/60/split_rotate"
path_dst125 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/125/split"
path_dst125_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/125/split_rotate"
path_dst250 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/250/split"
path_dst250_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/250/split_rotate"
path_dst500 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/500/split"
path_dst500_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/500/split_rotate"
path_dst1000 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/1000/split"
path_dst1000_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/1000/split_rotate"


# Loading exposure images into a list
rotate = [37,40,58,59,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,88,89,105,108,112,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128]
dirs = sorted(os.listdir(path))
i=0
in_list = []
final_list = []
for file in dirs:
    in_list.append(file)
    i+=1
    if (i%9==0):
        final_list.append(in_list)
        i=0
        in_list = []
i=0
j=113
count = 0
even = True
for img_fn in final_list:
    #print(img_fn)
    #print(j)
    j+=1
    count4000=0
    count2000=0
    count15=0
    count30=0
    count60=0
    count125=0
    count250=0
    count500=0
    count1000=0
    img_list = []
    exposure_times = []

    for img in img_fn:
        #print(img)

        exif = {}
        image = Image.open(os.path.join(path,img))
        for tag, value in image._getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]]=value
        
        if 'ExposureTime' in exif:
            extime=round(exif['ExposureTime'],6)
            if(abs(extime-0.00025)<0.000001 and count4000<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst4, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst4_rotate, "img"+str(j)+"_rotate.jpg"))
                count4000+=1

            elif(abs(extime-0.0005)<0.000001 and count2000<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst8,"img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst8_rotate, "img"+str(j)+"_rotate.jpg"))
                count2000+=1

            elif(abs(extime-0.06666666666667)<0.000001 and count15<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst15, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst15_rotate, "img"+str(j)+"_rotate.jpg"))
                count15+=1

            elif(abs(extime-0.03333333333333)<0.000001 and count30<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst30, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst30_rotate, "img"+str(j)+"_rotate.jpg"))
                count30+=1

            elif(abs(extime-0.0166666666666)<0.000001 and count60<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst60, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst60_rotate, "img"+str(j)+"_rotate.jpg"))
                count60+=1
             
            elif(abs(extime-0.008)<0.000001 and count125<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst125, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst125_rotate, "img"+str(j)+"_rotate.jpg"))
                count125+=1
                
            elif(abs(extime-0.004)<0.000001 and count250<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst250, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst250_rotate, "img"+str(j)+"_rotate.jpg"))
                count250+=1

            elif(abs(extime-0.002)<0.000001 and count500<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst500, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst500_rotate, "img"+str(j)+"_rotate.jpg"))
                count500+=1

            elif(abs(extime-0.001)<0.000001 and count1000<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst1000, "img"+str(j)+".jpg"))
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst1000_rotate, "img"+str(j)+"_rotate.jpg"))
                count1000+=1

            else:
                print("something wrong in image {}", format(j))
    
    if j in rotate and i<j:
        i=j
        j-=1
        even = False
    else:
        i=j
        even = True