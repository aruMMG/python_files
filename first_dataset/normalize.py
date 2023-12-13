import cv2
import numpy as np

path = '/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/exr/easy/hdr2.exr'
img = cv2.imread(path, cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
print(type(img))
maxim = np.max(img)
print(maxim)