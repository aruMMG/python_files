import cv2
import numpy as np


img1 = cv2.imread("/home/aru/phd/objective2/pbrt-v3/scenes/nakajima/nakajima_Al_smooth_scaled.exr", flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)

tonemap = cv2.createTonemap(gamma=2.2)
img = tonemap.process(img1)

# img = img1[200:800,200:800]
cv2.imwrite("/home/aru/phd/objective2/pbrt-v3/scenes/nakajima/Al_smooth_scaled_1024.png", img*255)