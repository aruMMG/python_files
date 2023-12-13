import os
import cv2

p1x = 4123
p1y = 1915
p2x = 3453
p2y = 1787
p3x = 2133
p3y = 1593
path = "/home/sakuni/phd/Experiments/hdr/calibration/test1/exr/hdr9.exr"
image = cv2.imread(path, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
im = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)

sum1x=0
sum1y=0
sum1z=0
for j in range(p1x-30,p1x+30):
    for i in range(p1y-30,p1y+30):
        sum1x+=im[i,j,0]
        sum1y+=im[i,j,1]
        sum1z+=im[i,j,2]
avg1x=sum1x/3600
avg1y=sum1y/3600
avg1z=sum1z/3600

sum2x=0
sum2y=0
sum2z=0
for j in range(p2x-30,p2x+30):
    for i in range(p2y-30,p2y+30):
        sum2x+=im[i,j,0]
        sum2y+=im[i,j,1]
        sum2z+=im[i,j,2]
avg2x=sum2x/3600
avg2y=sum2y/3600
avg2z=sum2z/3600

sum3x=0
sum3y=0
sum3z=0
for j in range(p3x-30,p3x+30):
    for i in range(p3y-30,p3y+30):
        sum3x+=im[i,j,0]
        sum3y+=im[i,j,1]
        sum3z+=im[i,j,2]
avg3x=sum3x/3600
avg3y=sum3y/3600
avg3z=sum3z/3600

print(avg1x, avg1y, avg1z)
print(avg2x, avg2y, avg2z)
print(avg3x, avg3y, avg3z)
