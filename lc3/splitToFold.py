import os
import glob
import shutil
from random import shuffle
import cv2


path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold"
path_60 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/60/1024"

img_hard = os.listdir(os.path.join(path,"hard"))
shuffle(img_hard)
img_easy = os.listdir(os.path.join(path,"easy"))
shuffle(img_easy)

num_of_img_hard = len(img_hard)
print(num_of_img_hard)
num_of_img_easy = len(img_easy)
print(num_of_img_easy)

i=0
j=0
for img in img_hard:
    print(img)
    img_path = os.path.join(path,"hard",img)
    label_path_split = os.path.join(path_60,"split/labels")
    label_path_split_rotate = os.path.join(path_60,"split_rotate/labels")

    name = os.path.splitext(img)[0]
    label_name = name+".txt"

    if os.path.exists(os.path.join(label_path_split,label_name)):
        label_path = os.path.join(label_path_split,label_name)
    elif os.path.exists(os.path.join(label_path_split_rotate,label_name)):
        label_path = os.path.join(label_path_split_rotate,label_name)
    else:
        print("label not available") 

    if i%(int(num_of_img_hard/5))==0:
        j+=1
    
    shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(j),"images/val"))
    shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(j),"labels/val"))

    for k in range(1,6):
        if k==j:
            continue
        else:
            shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(k),"images/train"))
            shutil.copy2(img_path,os.path.join(path,"folds","fold"+str(k),"images/train",name+"_copy.jpg"))
            shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(k),"labels/train",name+"_copy.txt"))
            shutil.copy2(label_path,os.path.join(path,"folds","fold"+str(k),"labels/train"))

    i+=1

i=0
j=0
for img in img_easy:
    img_path = os.path.join(path,"easy",img)
    label_path_split = os.path.join(path_60,"split/labels")
    label_path_split_rotate = os.path.join(path_60,"split_rotate/labels")

    name = os.path.splitext(img)[0]
    label_name = name+".txt"

    if os.path.exists(os.path.join(label_path_split,label_name)):
        label_path = os.path.join(label_path_split,label_name)
    elif os.path.exists(os.path.join(label_path_split_rotate,label_name)):
        label_path = os.path.join(label_path_split_rotate,label_name)
    else:
        print("label not available") 

    if i%(int(num_of_img_easy/5))==0:
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

