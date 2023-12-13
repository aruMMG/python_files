import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/exr/1024/split_rotate/images/img73_rotate.exr"
path_best_exp = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/split_rotate/images/img73_rotate.jpg"
save_path = "/home/sakuni/phd/Experiments/hdr/python/lc3/histogram/hdr"
image = cv2.imread(path, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
# image = cv2.imread(path)
img = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)[:,:,1].astype(int)
# print(np.max(img))
image_best_exp = cv2.imread(path_best_exp)
for i in range(1024):
    for j in range(1024):
        if img[i,j]<50:
            image[i,j,:]=0
            image_best_exp[i,j,:]=0
cv2.imwrite(os.path.join(save_path, "img2_rotate_100_threshold50.exr"), image)
cv2.imwrite(os.path.join(save_path, "img2_rotate_100_threshold50.png"), image_best_exp)
a = img[img>=50]
histogram, bin_edges = np.histogram(a, bins=125)
# cv2.imwrite(os.path.join(save_path,"img1.exr"), image)
# histogram, bin_edges = np.histogram(img, bins=256)
print(histogram)
print(bin_edges)
plt.figure()
plt.xlabel("Luminance value")
plt.ylabel("Pixel count")
plt.plot(bin_edges[0:-1], histogram)
plt.savefig(os.path.join(save_path, "img2_rotate_100_threshold50_histogram.png"))
