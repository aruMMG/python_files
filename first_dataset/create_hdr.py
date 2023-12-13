import os
from PIL import Image
from PIL.ExifTags import TAGS

import cv2 as cv
import numpy as np
# Loading exposure images into a list
path = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/2"
path_ldr = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/ldr_exr"
path_hdr = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/exr"
#extime_list = [round(0.06666666666667,6), round(0.3333333333333,6), round(0.0166666666666,6), round(0.008,6), round(0.004,6), round(0.002,6)]
dirs = sorted(os.listdir(path))
i=0
in_list = []
final_list = []
for file in dirs:
    in_list.append(file)
    #print(in_list)
    i+=1
    if (i%11==0):
        final_list.append(in_list)
        i=0
        in_list = []
#print(final_list)


j=113
for img_fn in final_list:
    #print(img_fn)
    #print(j)
    j+=1
    img_list = []
    exposure_times = []
    count2=0
    count4=0
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
            
            if (abs(extime-0.125)<0.000001 and count8==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count8+=1                
                
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

            elif(abs(extime-0.0005)<0.000001 and count2000==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count2000+=1
            
            elif(abs(extime-0.25)<0.000001 and count4==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count4+=1

            elif(abs(extime-0.5)<0.000001 and count2==0):
                im=cv.imread(os.path.join(path, img))

                h,w,c=im.shape
                if (h<w):
                    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
                exposure_times.append(extime)
                img_list.append(im)
                count2+=1
            else:
                break

    if(len(exposure_times)!=11):
        continue                                           
    assert (len(img_list)==len(exposure_times)), "Exposuretime not available for some image"
    assert (len(exposure_times)==11), "Exposuretime not available for some image"

    exposure_times=np.asarray(exposure_times, dtype=np.float32)

    calibrate = cv.createCalibrateDebevec()
    response = calibrate.process(img_list, exposure_times)

    merge_debevec = cv.createMergeDebevec()
    hdr = merge_debevec.process(img_list, exposure_times, response)
    # merge_robertson = cv.createMergeRobertson()
    # hdr_robertson = merge_robertson.process(img_list,exposure_times, response)

    tonemap1 = cv.createTonemap(gamma=2.2)
    ldr = tonemap1.process(hdr)
    # ldr_robertson=tonemap1.process(hdr_robertson)

    # merge_mertens = cv.createMergeMertens()
    # fusion = merge_mertens.process(img_list)

    print(exposure_times)
    # cv.imwrite(os.path.join(path_fusion, 'fusion'+str(j)+'.png'), fusion * 255)
    cv.imwrite(os.path.join(path_ldr, 'ldr'+str(j)+'.png'), ldr * 255)
    cv.imwrite(os.path.join(path_hdr, 'hdr'+str(j)+'.exr'), hdr)

