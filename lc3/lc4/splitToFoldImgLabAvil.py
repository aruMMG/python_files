import os
import glob
import shutil
from random import shuffle
import cv2
import re

path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/big_small_dataset"

def makeFolder(path_name,name):
    if not os.path.exists(os.path.join(path_name,name)):
        os.mkdir(os.path.join(path_name,name))

import math
makeFolder(path, "folds")
for i in range(1,6):
    fold_name = "fold"+str(i)
    makeFolder(os.path.join(path, "folds"), fold_name)
    makeFolder(os.path.join(path, "folds", fold_name), "images")
    makeFolder(os.path.join(path, "folds", fold_name, "images"), "train")
    makeFolder(os.path.join(path, "folds", fold_name, "images"), "val")
    makeFolder(os.path.join(path, "folds", fold_name), "labels")
    makeFolder(os.path.join(path, "folds", fold_name, "labels"), "train")
    makeFolder(os.path.join(path, "folds", fold_name, "labels"), "val")

img_small = os.listdir(os.path.join(path,"small/images"))
shuffle(img_small)
img_big = os.listdir(os.path.join(path,"big/images"))
shuffle(img_big)

num_of_img_small = len(img_small)
print(num_of_img_small)
num_of_img_big = len(img_big)
print(num_of_img_big)
big_small_list = [62, 67,69,71,72,73,75,76,79,81,105,108]
i=0
j=0
print(len(big_small_list))
print(math.ceil((num_of_img_small-len(big_small_list))/10))

for img in img_small:
    # print(img)
    img_path = os.path.join(path,"small/images",img)
    label_path = os.path.join(path,"small/labels")


    name = os.path.splitext(img)[0]
    num = re.search(r"\d+", name)
    if name.endswith("_rotate") or int(num.group()) in big_small_list:
        # print(int(num.group()))
        continue
    label_name = name+".txt"
    img_rotate_path = (os.path.join(path, "small/images", name+"_rotate.jpg"))
    label_rotate_name = name + "_rotate.txt"
    label_rotate_path = os.path.join(label_path, label_rotate_name)
    label_path = os.path.join(label_path,label_name)
    if i%math.ceil((num_of_img_small-2*len(big_small_list))/10)==0:
        j+=1
    
    shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(j),"images/val"))
    shutil.copy2(img_rotate_path,os.path.join(path,"folds","fold"+str(j),"images/val"))
    shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(j),"labels/val"))
    shutil.copy2(label_rotate_path,os.path.join(path,"folds","fold"+str(j),"labels/val"))

    for k in range(1,6):
        if k==j:
            continue
        else:
            shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(k),"images/train"))
            shutil.copy2(img_rotate_path,os.path.join(path,"folds","fold"+str(k),"images/train"))
            # shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(k),"images/train",name+"_copy.jpg"))
            # shutil.copy2(img_rotate_path,os.path.join(path,"folds","fold"+str(k),"images/train",name+"_rotate_copy.jpg"))
            # shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(k),"labels/train",name+"_copy.txt"))
            # shutil.copy2(label_rotate_path,os.path.join(path,"folds","fold"+str(k),"labels/train",name+"_rotate_copy.txt"))
            shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(k),"labels/train"))
            shutil.copy2(label_rotate_path,os.path.join(path,"folds","fold"+str(k),"labels/train"))

    i+=1

i=0
j=0
for img in img_big:
    print(img)

    img_path = os.path.join(path,"big/images",img)
    label_path = os.path.join(path,"big/labels")


    name = os.path.splitext(img)[0]
    label_name = name+".txt"


    label_path = os.path.join(label_path,label_name)

    if i%(int(num_of_img_big/5))==0:
        j+=1
    
    shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(j),"images/val"))
    shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(j),"labels/val"))

    for k in range(1,6):
        if k==j:
            continue
        else:
            shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(k),"images/train"))
            shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(k),"labels/train"))

    i+=1
import random
random.shuffle(big_small_list)
i = 0
j=0
for img_num in big_small_list:
    if i%2==0 and i<9:
        j+=1
    img_path = os.path.join(path, "small/images","img"+str(img_num)+".jpg")
    img_rotate_path = os.path.join(path, "small/images","img"+str(img_num)+"_rotate.jpg")
    label_path = os.path.join(path,"small/labels", "img"+str(img_num)+".txt")
    label_rotate_path = os.path.join(path,"small/labels", "img"+str(img_num)+"_rotate.txt")

    shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(j),"images/val"))
    shutil.copy2(img_rotate_path,os.path.join(path,"folds","fold"+str(j),"images/val"))
    shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(j),"labels/val"))
    shutil.copy2(label_rotate_path,os.path.join(path,"folds","fold"+str(j),"labels/val"))
    for k in range(1,6):
        if k==j:
            continue
        else:
            shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(k),"images/train"))
            shutil.copy2(img_rotate_path,os.path.join(path,"folds","fold"+str(k),"images/train"))
            # shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(k),"images/train","img"+str(img_num)+"_copy.jpg"))
            # shutil.copy2(img_rotate_path,os.path.join(path,"folds","fold"+str(k),"images/train","img"+str(img_num)+"_rotate_copy.jpg"))
            # shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(k),"labels/train","img"+str(img_num)+"_copy.txt"))
            # shutil.copy2(label_rotate_path,os.path.join(path,"folds","fold"+str(k),"labels/train","img"+str(img_num)+"_rotate_copy.txt"))
            shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(k),"labels/train"))
            shutil.copy2(label_rotate_path,os.path.join(path,"folds","fold"+str(k),"labels/train"))
    i+=1