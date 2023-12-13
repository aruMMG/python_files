import cv2 as cv
import numpy
import glob
import shutil
import os
import re
import numpy as np
from random import shuffle

path_double = glob.glob('/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/double/images/*.jpg')
path_set1 = glob.glob('/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/set1/images/*.jpg')


path_all = '/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/all_1024/*.jpg'
img_path = '/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/all_1024'
path_easy = '/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/easy'
list_all = []
for img in glob.glob(path_all):
    _, name = os.path.split(img)
    list_all.append(name)
list_double = []
for img in path_double:
    _, name = os.path.split(img)
    list_double.append(name)
list_set1 = []
for img in path_set1:
    _, name = os.path.split(img)
    list_set1.append(name)

for element in list_double:
    if element in list_all:
        list_all.remove(element)

for element in list_set1:
    if element in list_all:
        list_all.remove(element)
print(len(list_all))
shuffle(list_all)
list_easy = list_all[0:80]

for img in list_easy:
    shutil.copy2(os.path.join(img_path,img), path_easy)

