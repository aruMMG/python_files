import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

import cv2 as cv
import numpy as np


path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/split"
path_dst4 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/4/split"
path_dst4_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/4/split_rotate"
path_dst8 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/8/split"
path_dst8_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/8/split_rotate"
path_dst15 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/15/split"
path_dst15_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/15/split_rotate"
path_dst30 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/30/split"
path_dst30_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/30/split_rotate"
path_dst60 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/split"
path_dst60_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/split_rotate"
path_dst125 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/125/split"
path_dst125_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/125/split_rotate"
path_dst250 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/250/split"
path_dst250_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/250/split_rotate"
path_dst500 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/500/split"
path_dst500_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/500/split_rotate"
path_dst1000 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/1000/split"
path_dst1000_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/1000/split_rotate"


# Loading exposure images into a list

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

j=0
even = True
for img_fn in final_list:
    #print(img_fn)
    #print(j)
    if even:
        j+=1
        count4=0
        count8=0
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
            if(abs(extime-0.25)<0.000001 and count4<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst4, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst4_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count4+=1

            elif(abs(extime-0.125)<0.000001 and count8<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst8,"img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst8_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count8+=1

            elif(abs(extime-0.06666666666667)<0.000001 and count15<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst15, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst15_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count15+=1

            elif(abs(extime-0.03333333333333)<0.000001 and count30<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst30, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst30_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count30+=1

            elif(abs(extime-0.0166666666666)<0.000001 and count60<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst60, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst60_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count60+=1
             
            elif(abs(extime-0.008)<0.000001 and count125<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst125, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst125_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True   
                count125+=1
                
            elif(abs(extime-0.004)<0.000001 and count250<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst250, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst250_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count250+=1

            elif(abs(extime-0.002)<0.000001 and count500<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst500, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst500_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count500+=1

            elif(abs(extime-0.001)<0.000001 and count1000<2):
                if even:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst1000, "img"+str(j)+".jpg"))
                    even = False
                else:
                    shutil.copy2(os.path.join(path,img),os.path.join(path_dst1000_rotate, "img"+str(j)+"_rotate.jpg"))
                    even = True
                count1000+=1

            else:
                print("something wrong in image {}", format(j))