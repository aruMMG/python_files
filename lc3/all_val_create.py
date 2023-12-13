import os
import glob
import shutil
import re

path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/exr/1024/lc3_hdr_folds/fold5"
search_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/exr/1024"
label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/60/1024"
ext = ".exr"

def makeFolder(path_name,name):
    if not os.path.exists(os.path.join(path_name,name)):
        os.mkdir(os.path.join(path_name,name))


makeFolder(os.path.join(path, "images"), "test_all")
makeFolder(os.path.join(path, "labels"), "test_all")

for img in glob.glob(os.path.join(path, "images/val", "*"+ext)):
    _, img_name = os.path.split(img)
    shutil.copy2(img, os.path.join(path, "images/test_all"))
    name_only = os.path.splitext(img_name)[0]
    shutil.copy2(os.path.join(path, "labels/val", name_only+".txt"), os.path.join(path, "labels/test_all"))
    if name_only.endswith("_rotate"):
        findImageName = name_only.replace("_rotate", "")
        if os.path.isfile(os.path.join(search_path, "split/images", findImageName+ext)):
            shutil.copy2(os.path.join(search_path, "split/images", findImageName+ext), os.path.join(path, "images/test_all"))
            shutil.copy2(os.path.join(label_path, "split/labels", findImageName+".txt"), os.path.join(path, "labels/test_all"))
        else:
            print("Rotate image has no first image for image name {}".format(name_only))
    else:
        findImageName = name_only + "_rotate"
        if os.path.isfile(os.path.join(search_path, "split_rotate/images", findImageName+ext)):
            shutil.copy2(os.path.join(search_path, "split_rotate/images", findImageName+ext), os.path.join(path, "images/test_all"))
            shutil.copy2(os.path.join(label_path, "split_rotate/labels", findImageName+".txt"), os.path.join(path, "labels/test_all"))
        else:
            print("image has no first rotate image for name {}".format(name_only))
        
