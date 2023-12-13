import cv2
import glob
from PIL import Image
import numpy as np
import torch
from torchvision import transforms
import os
import re


outPath = '/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/wardHistAdj/1024/split/images'
path = glob.glob('/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/wardHistAdj/split/*.png')

print(len(path))
image_list = []
for img in path:
    img_path, name_exr =os.path.split(img)
    image = cv2.imread(img, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
    h,w,c = image.shape
    if h<w:
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img_crop=image[1650:4590,500:3440]
    img_exr=cv2.resize(img_crop, (1024,1024), interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(outPath, name_exr), img_exr)
    
outPath_rotate = '/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/wardHistAdj/1024/split_rotate/images'
path_rotate = glob.glob('/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/wardHistAdj/split_rotate/*.png')

print(len(path))
image_list = []
for img in path_rotate:
    img_path, name_exr =os.path.split(img)
    image = cv2.imread(img, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
    h,w,c = image.shape
    if h<w:
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img_crop=image[1650:4590,500:3440]
    img_exr=cv2.resize(img_crop, (1024,1024), interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(outPath_rotate, name_exr), img_exr)
 