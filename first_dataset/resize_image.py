import cv2
import glob
from PIL import Image
import numpy as np
import torch
from torchvision import transforms
import os
from pathlib import Path
import re


#outPath_ldr = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/1024/102/exr_ldr"
outPath = '/home/sakuni/phd/Experiments/hdr/dataset/dataset4_all_exposure/500/images_1024'

path = glob.glob('/home/sakuni/phd/Experiments/hdr/dataset/dataset4_all_exposure/500/images/*.jpg')
#path_ldr = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/full/ldr_exr/11"
#path_ldr = glob.glob('/home/sakuni/phd/Experiments/hdr/ldr_exr/*.png')
print(len(path))
image_list = []
k=1
for img in path:
    img_path, name_exr =os.path.split(img)
    #num = re.findall(r'[0-9]+', name_exr)
    
    #name_ldr = 'ldr'+str(num[0])+'.png'
    #img_path_ldr = os.path.join(path_ldr, name_ldr)

    image = cv2.imread(img, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
    h,w,c = image.shape
    if h<w:
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #image_ldr = cv2.imread(img_path_ldr)

    #print(type(image[3050,3050,1]))
    
    img_crop=image[700:4040,0:3340]
    #img_ldr_crop=image_ldr[700:4040,0:3340]
    
    img_exr=cv2.resize(img_crop, (1024,1024), interpolation=cv2.INTER_AREA)
    #img_ldr=cv2.resize(img_ldr_crop, (1024,1024), interpolation=cv2.INTER_AREA)

    #print(im1.shape)
    #area=(800,300,4300,3800)
    #croped_img=image.crop(area)
    #print(croped_img.shape)
    #newsize=(3500,2625)
    #im1=image.resize(newsize)
    cv2.imwrite(os.path.join(outPath, name_exr), img_exr)
    #cv2.imwrite(os.path.join(outPath_ldr, name_ldr), img_ldr)
    
    k+=1
