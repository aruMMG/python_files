from ast import Break
import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
import glob
import cv2 as cv
import numpy as np
# Loading exposure images into a list



def processing(path, img, counts, loc):
    im=cv.imread(os.path.join(path, img))

    h,w,c=im.shape
    if (h<w):
        im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
    counts[loc]=1   
    return im, counts

def find_time(path, img, counts, white_path=False):
    exif = {}
    img_path = os.path.join(path,img)
    image = Image.open(img_path)
    if white_path:
        img_name = os.path.basename(img_path)
        fol_name = img_path.split("/")[-2]
        img = os.path.join(white_path, fol_name, img_name)
    print(image.size)
    for tag, value in image._getexif().items():
        if tag in TAGS:
            exif[TAGS[tag]]=value
    
    if 'ExposureTime' in exif:
        extime=round(exif['ExposureTime'],6)
        
        if(abs(extime-0.06666666666667)<0.000001 and counts[0]==0):
            im, counts = processing(path, img, counts, 0)
            return extime, im, counts

        elif(abs(extime-0.03333333333333)<0.000001 and counts[1]==0):
            im, counts = processing(path, img, counts, 1)
            return extime, im, counts

        elif(abs(extime-0.0166666666666)<0.000001 and counts[2]==0):
            im, counts = processing(path, img, counts, 2)
            return extime, im, counts
            
        elif(abs(extime-0.008)<0.000001 and counts[3]==0):
            im, counts = processing(path, img, counts, 3)
            return extime, im, counts
            
        elif(abs(extime-0.004)<0.000001 and counts[4]==0):
            im, counts = processing(path, img, counts, 4)
            return extime, im, counts

        elif(abs(extime-0.002)<0.000001 and counts[5]==0):
            im, counts = processing(path, img, counts, 5)
            return extime, im, counts
        elif(abs(extime-0.001)<0.000001 and counts[6]==0):
            im, counts = processing(path, img, counts, 6)
            return extime, im, counts
        
        elif(abs(extime-0.0005)<0.000001 and counts[7]==0):
            im, counts = processing(path, img, counts, 7)
            return extime, im, counts

        elif (abs(extime-0.00025)<0.000001 and counts[8]==0):
            im, counts = processing(path, img, counts, 8)
            return extime, im, counts
            
        else:
            return False, False, counts

def separateImages(dirs, num_exp):
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
    return final_list
def from_folders(path, dirs, num_exp):
    in_list, final_list = [], []
    fold_img_dict = {}

    img_list = os.listdir(os.path.join(path, dirs[0]))
    for img_name in img_list:    
        in_list.append(os.path.join(path, dirs[0], img_name))
        for idx in range(1,num_exp):
            img_selected = os.path.join(path, dirs[idx], img_name)
            in_list.append(img_selected)
        final_list.append(in_list)
        in_list = []
    return final_list

def from_folders_single_image(path, dirs, num_exp, img_name = "img6.jpg"):
    in_list, final_list = [], []
    fold_img_dict = {}

    img_list = os.listdir(os.path.join(path, dirs[0], "split"))
    for img in img_list:    
        if img_name == img:            
            in_list.append(os.path.join(path, dirs[0], "split", img))
            for idx in range(1,num_exp):
                img_selected = os.path.join(path, dirs[idx], "split", img_name)
                in_list.append(img_selected)
            final_list.append(in_list)
            in_list = []
    return final_list

def create_hdr(path, img_group, save_path, isSeparate=False, img_white=False):
    img_list = []
    exposure_times = []
    counts = np.zeros(9)
    for img in img_group:
        #print(img)
        if isSeparate:
            exp_time, I, counts = find_time(path, img, counts, img_white=img_white)
        else:
            exp_time, I, counts = find_time(path, img, counts,white_path=img_white)

        if exp_time:
            exposure_times.append(exp_time)
            img_list.append(I)
        else:
            Break

    assert (len(img_list)==len(exposure_times)), "Exposuretime not available for some image"
    assert (len(exposure_times)==num_exp), "Exposuretime not available for some image"

    exposure_times=np.asarray(exposure_times, dtype=np.float32)

    calibrate = cv.createCalibrateDebevec()
    response = calibrate.process(img_list, exposure_times)

    merge_debevec = cv.createMergeDebevec()
    hdr = merge_debevec.process(img_list, exposure_times, response)

    cv.imwrite(save_path, hdr)




def main(path, path_hdr_rotate, path_hdr, num_exp=9, isOnePlace = True, rotate = False, img_white = False, oneImg=False):
    dirs = sorted(os.listdir(path))
    
    if isOnePlace:
        final_list = separateImages(dirs, num_exp)
    elif oneImg:
        final_list = from_folders_single_image(path, dirs, num_exp)
    else:
        final_list = from_folders(path, dirs, num_exp)
    j=0
    even = True
    for img_group in final_list:
        if even:
            j+=1
            if rotate:
                even=False
            img_name = os.path.basename(img_group[1]).split(".")[0]
            save_path = os.path.join(path_hdr,img_name +'.exr')
            if img_white:
                create_hdr(path, img_group, save_path, img_white=img_white)        
            else:
                create_hdr(path, img_group, save_path)        
        else:
            save_path = os.path.join(path_hdr, 'hdr'+str(j)+'_rotate.exr')
            create_hdr(path, img_group, save_path)        
            even = True
        



if __name__=="__main__":
    
    path = "/home/aru/phd/objective2/dataset/safe_single_exp"
    path_hdr_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/exr/safe_split_rotate"
    save_path = "/home/aru/phd/objective2/dataset/white_balance/hdr/safe_single_exp"

    num_exp = 9
    
    main(path, path_hdr_rotate, save_path, num_exp=num_exp, isOnePlace=False, img_white="/home/aru/phd/objective2/dataset/white_balance/safe_single_exp")
    # import glob
    # img = os.listdir(path)
    # create_hdr(path, img, save_path)