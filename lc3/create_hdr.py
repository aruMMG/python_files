import os
from PIL import Image
from PIL.ExifTags import TAGS
import glob
import cv2 as cv
import numpy as np
# Loading exposure images into a list
path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/new_crack"
path_hdr_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/exr/split_rotate"
path_hdr = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/exr/split"
num_exp = 9
#extime_list = [round(0.06666666666667,6), round(0.3333333333333,6), round(0.0166666666666,6), round(0.008,6), round(0.004,6), round(0.002,6)]
dirs = sorted(os.listdir(path))
i=0
in_list = []
final_list = []
for file in dirs:
    in_list.append(file)
    #print(in_list)
    i+=1
    if (i%num_exp==0):
        final_list.append(in_list)
        i=0
        in_list = []
#print(final_list)

count=0
j=113
rotate = [37,40,58,59,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,88,89,105,108,112,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128]
for img_fn in final_list:
    #print(img_fn)
    #print
    j+=1
    img_list = []
    exposure_times = []
    count2=0
    count4000=0
    count8=0
    count15=0
    count30=0
    count60=0
    count125=0
    count250=0
    count500=0
    count1000=0
    count2000=0
    for img in img_fn:
        #print(img)

        exif = {}
        image = Image.open(os.path.join(path,img))
        for tag, value in image._getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]]=value
        
        if 'ExposureTime' in exif:
            extime=round(exif['ExposureTime'],6)
            
            if (abs(extime-0.00025)<0.000001 and count4000==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count4000+=1                
                
            elif(abs(extime-0.06666666666667)<0.000001 and count15==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count15+=1

            elif(abs(extime-0.03333333333333)<0.000001 and count30==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count30+=1

            elif(abs(extime-0.0166666666666)<0.000001 and count60==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count60+=1
             
            elif(abs(extime-0.008)<0.000001 and count125==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count125+=1
                
            elif(abs(extime-0.004)<0.000001 and count250==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count250+=1

            elif(abs(extime-0.002)<0.000001 and count500==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count500+=1
            elif(abs(extime-0.001)<0.000001 and count1000==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count1000+=1

            # elif(abs(extime-0.0005)<0.000001 and count2000==0):
            #     im=cv.imread(os.path.join(path, img))

            #     h,w,c=im.shape
            #     if (h<w):
            #         im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
            #     exposure_times.append(extime)
            #     img_list.append(im)
            #     count2000+=1
            
            elif(abs(extime-0.0005)<0.000001 and count2000==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count2000+=1

            # elif(abs(extime-0.5)<0.000001 and count2==0):
            #     im=cv.imread(os.path.join(path, img))

            #     h,w,c=im.shape
            #     if (h<w):
            #         im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
            #     exposure_times.append(extime)
            #     img_list.append(im)
            #     count2+=1
            else:
                break

    if(len(exposure_times)!=num_exp):
        continue                                           
    assert (len(img_list)==len(exposure_times)), "Exposuretime not available for some image"
    assert (len(exposure_times)==num_exp), "Exposuretime not available for some image"
    print("all iimage read")
    if j in rotate and count == 1:
        print("hdr conversion started")
        exposure_times=np.asarray(exposure_times, dtype=np.float32)

        calibrate = cv.createCalibrateDebevec()
        response = calibrate.process(img_list, exposure_times)

        merge_debevec = cv.createMergeDebevec()
        hdr = merge_debevec.process(img_list, exposure_times, response)
        cv.imwrite(os.path.join(path_hdr_rotate, 'img'+str(j)+'_rotate.exr'), hdr)
        count = 0    
    elif j not in rotate or count==0:
        print("hdr conversion started")
        exposure_times=np.asarray(exposure_times, dtype=np.float32)

        calibrate = cv.createCalibrateDebevec()
        response = calibrate.process(img_list, exposure_times)

        merge_debevec = cv.createMergeDebevec()
        hdr = merge_debevec.process(img_list, exposure_times, response)

        print("write hdr image")
        cv.imwrite(os.path.join(path_hdr, 'img'+str(j)+'.exr'), hdr)
        if j in rotate:
            count = 1
            j-=1           
