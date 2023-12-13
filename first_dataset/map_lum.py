import cv2
import numpy as np
import os

path_save = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/full/exr/map_11"

def func(X, A,b):
    res = A*(X**b)
    #print(res.shape)
    return res

A_X = 0.01303146973899461
b_X=1.8174542665407063
A_Y = 0.01327997309054267
b_Y = 1.8005617092226287
A_Y2 = 0.010605571799403447
b_Y2 = 1.8291475626211091
c_Y2 = 88.37997911110513
A_Z = 0.006535697680821371
b_Z = 1.802770221087039
path = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/full/exr/11/hdr62.exr"
image = cv2.imread(path, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)

image = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)

print(image[3000,1600,1])
#image[:,:,1] = func(image[:,:,1], A_Y, b_Y)
image[:,:,0] = func(image[:,:,0], A_Y, b_Y)
#image[:,:,2] = func(image[:,:,2], A_Z, b_Z)
print(image[3000,1600,1])
image = cv2.cvtColor(image, cv2.COLOR_XYZ2BGR)
cv2.imwrite(os.path.join(path_save, 'hdr62.exr'), image)