import xlrd
from xlutils.copy import copy
import os
import cv2

path_xl = "/home/sakuni/phd/Experiments/hdr/calibration/test4/luminance_reading4.xlsx"
path_xl_save = "/home/sakuni/phd/Experiments/hdr/calibration/test4/luminance_reading4a.xlsx"
path = "/home/sakuni/phd/Experiments/hdr/calibration/test4"

# Choose file and sheet
wb = xlrd.open_workbook(path_xl)
sheet = wb.sheet_by_name("Sheet4")

# Select the column index
arrayofvalue = sheet.col_values(6)
arrayofvalue1 = sheet.col_values(7)


w_index = 9

# select sheet to write
w_wb = copy(wb)
w_sheet = w_wb.get_sheet(3)

# Remove heading
arrayofvalue = arrayofvalue[2:35]
arrayofvalue = [int(x) for x in arrayofvalue]
#assert (type(arrayofvalue[0])==type(1)), "list contain non integer type"
arrayofvalue1 = arrayofvalue1[2:35]
#assert (type(arrayofvalue1[0])==type(1)), "list contain non integer type"
arrayofvalue1 = [int(x) for x in arrayofvalue1]

im_no = 1
i=0
while i<len(arrayofvalue1):

    p1x = arrayofvalue[i]
    p1y = arrayofvalue1[i]
    p2x = arrayofvalue[i+1]
    p2y = arrayofvalue1[i+1]
    p3x = arrayofvalue[i+2]
    p3y = arrayofvalue1[i+2]

    image = cv2.imread(os.path.join(path, "exr", "hdr"+str(im_no)+".exr"), flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
    ldr_img = cv2.imread(os.path.join(path,"marked_test", "img"+str(im_no)+".jpg"))
    
    if image.shape!=ldr_img.shape:
        image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
    
    assert (image.shape==ldr_img.shape), "HDR LDR image size does not match"
    
    im = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)

    sum1x=0
    sum1y=0
    sum1z=0
    for j in range(p1x-30,p1x+30):
        for k in range(p1y-30,p1y+30):
            sum1x+=im[k,j,0]
            sum1y+=im[k,j,1]
            sum1z+=im[k,j,2]
    avg1x=sum1x/3600
    avg1y=sum1y/3600
    avg1z=sum1z/3600

    sum2x=0
    sum2y=0
    sum2z=0
    for j in range(p2x-30,p2x+30):
        for k in range(p2y-30,p2y+30):
            sum2x+=im[k,j,0]
            sum2y+=im[k,j,1]
            sum2z+=im[k,j,2]
    avg2x=sum2x/3600
    avg2y=sum2y/3600
    avg2z=sum2z/3600

    sum3x=0
    sum3y=0
    sum3z=0
    for j in range(p3x-30,p3x+30):
        for k in range(p3y-30,p3y+30):
            sum3x+=im[k,j,0]
            sum3y+=im[k,j,1]
            sum3z+=im[k,j,2]
    avg3x=sum3x/3600
    avg3y=sum3y/3600
    avg3z=sum3z/3600

    print(avg1x, avg1y, avg1z)
    print(avg2x, avg2y, avg2z)
    print(avg3x, avg3y, avg3z)

    # Select write position
    w_sheet.write(i+2, w_index, avg1x)
    w_sheet.write(i+2, w_index+1, avg1y)
    w_sheet.write(i+2, w_index+2, avg1z)

    w_sheet.write(i+1+2, w_index, avg2x)
    w_sheet.write(i+1+2, w_index+1, avg2y)
    w_sheet.write(i+1+2, w_index+2, avg2z)
    
    w_sheet.write(i+2+2, w_index, avg3x)
    w_sheet.write(i+2+2, w_index+1, avg3y)
    w_sheet.write(i+2+2, w_index+2, avg3z)

    i+=3
    im_no+=1

w_wb.save(path_xl_save)
