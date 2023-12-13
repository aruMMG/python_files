import numpy as np
import cv2
import os
import glob
path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/split_rotate/images"
path_save = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/split_rotate_threshold"

for img_path in glob.glob(os.path.join(path,"*.jpg")):
    _,name_with_ext = os.path.split(img_path)
    name_only = os.path.splitext(name_with_ext)[0]
    save_name = name_only+".png"
    
    img_bgr = cv2.imread(img_path)
    img_lum = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2XYZ)
    w,h,c = img_bgr.shape
    for i in range(w):
        for j in range(h):
            if np.max(img_lum[i,j,1])>220:
                img_bgr[i,j,:]=255

    # img = cv2.cvtColor(img_bgr, cv2.COLOR_XYZ2BGR)
    cv2.imwrite(os.path.join(path_save,save_name),img_bgr)