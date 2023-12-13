"""
Give path to split and split rotate folder. and a reference to 30_fold path
It will take images from each files and create folds and save to indivisual folds as 30_folds
Copy the labels from 30_folds
Only generate train and val folder for images
check the image extensions before applying
"""

import os
import shutil
import glob
import re
from utils import makeFolder

image_path = "/home/aru/phd/hdr/dataset/hdr/split/images"
image_path_rotate = "/home/aru/phd/hdr/dataset/hdr/split_rotate/images"
fold_path = "/home/aru/phd/hdr/may24/yolov5_hdr/lc4_hdr_folds"
path_30 = "/home/aru/phd/hdr/dataset/lc4/lc4_30_folds"
path = "/home/aru/phd/hdr/dataset/lc4"

img_hard = os.listdir(os.path.join(path,"small/images"))


for i in range(1,6):
    makeFolder(fold_path, "fold"+str(i))
    makeFolder(os.path.join(fold_path,"fold"+str(i)),"images")
    makeFolder(os.path.join(fold_path,"fold"+str(i),"images"), "train")
    makeFolder(os.path.join(fold_path,"fold"+str(i),"images"), "val")


j=0
while j<5:
    j+=1
    label_path = os.path.join(path_30, "fold"+str(j), "labels")
    label_save_path = os.path.join(fold_path,"fold"+str(j),"labels")
    shutil.copytree(label_path,label_save_path)

    image_path_30 = os.path.join(path_30, "fold"+str(j),"images/val","*.jpg")

    for img in glob.glob(image_path_30):
        copy = False
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]

        image_num = re.search(r"\d+", name_only)
        if name_with_ext in img_hard:
            copy = True
        image_name = name_only+".exr"
        print(image_path, image_name)
        if os.path.exists(os.path.join(image_path,image_name)):
            full_image_path = os.path.join(image_path, image_name)
            
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "val"))

            for num in range(1,6):
                if j==num:
                    continue
                elif copy:
                    shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))
                    shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train",name_only+"_copy.exr"))
                else:
                    shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))

        elif os.path.exists(os.path.join(image_path_rotate,image_name)):
            full_image_path = os.path.join(image_path_rotate, image_name)
            
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "val"))


            for num in range(1,6):
                if j==num:
                    continue
                elif copy:
                    shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))
                    shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train",name_only+"_copy.exr"))
                else:
                    shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))



    
        else:
            print("image not available")

        
