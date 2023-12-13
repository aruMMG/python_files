import numpy as np
import cv2
img = np.array([[3,3,1,5,6,3],
                [6,5,12,4,5,5],
                [4,6,7,2,7,6],
                [4,2,8,9,5,7],
                [5,6,3,8,9,8],
                [5,6,3,8,9,8]])
imgCopy = np.uint8(img)
avg, std = img.mean(), img.std()
img = (img-avg)/std
kernel = np.array([[-1,-1,1,1]])
print(img)
img_masked = np.abs(cv2.filter2D(img, ddepth=-1, kernel=kernel))

print(img_masked)