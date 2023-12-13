import os
import shutil
import numpy as np

def list_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

def subset_array(arr):
    result = []
    found_val = False
    
    for element in arr:
        if element == "val":
            found_val = True
        if not found_val:
            result.append(element)
    
    return result

exr = False
if exr:
    directory1 = "/home/aru/phd/objective2/dataset/images/small/"
    directory2 = "/home/aru/phd/objective2/dataset/images/small_rotate/"
    directory3 = "/home/aru/phd/objective2/dataset/images/big/"
    label_directory = "/home/aru/phd/objective2/dataset/labels/"



    # Create a list to store all file paths
    file_paths = []

    # Function to recursively list all file paths in a directory


    # List files in each of the three directories
    list_files_in_directory(directory1)
    list_files_in_directory(directory2)
    list_files_in_directory(directory3)
else:
    directory1 = "/home/aru/phd/objective2/dataset/single_exp/30/1024/split/images/"
    directory2 = "/home/aru/phd/objective2/dataset/single_exp/30/1024/split_rotate/images/"
    label_directory = "/home/aru/phd/objective2/dataset/labels/"



    # Create a list to store all file paths
    file_paths = []

    # List files in each of the three directories
    list_files_in_directory(directory1)
    list_files_in_directory(directory2)

import glob

fold_path = "/home/aru/yolov5_hdr/datasets/10_real"

for i in range(1,6):
    csv_fold = os.path.join(fold_path, str(i)+".csv")
    os.mkdir(os.path.join(fold_path, f"fold{i}"))
    os.mkdir(os.path.join(fold_path, f"fold{i}/images"))
    os.mkdir(os.path.join(fold_path, f"fold{i}/images/train"))
    os.mkdir(os.path.join(fold_path, f"fold{i}/labels"))
    os.mkdir(os.path.join(fold_path, f"fold{i}/labels/train"))

    file = np.loadtxt(csv_fold,delimiter=",", dtype=str)
    file = subset_array(file)
    for path in file_paths:
        name = os.path.basename(path).split(".")[0]
        if name in file:
            if exr:
                shutil.copy(path, os.path.join(fold_path, f"fold{i}/images/train", name+".exr"))
            else:
                shutil.copy(path, os.path.join(fold_path, f"fold{i}/images/train", name+".jpg"))
            shutil.copy(os.path.join(label_directory, name+".txt"), os.path.join(fold_path, f"fold{i}/labels/train", name+".txt"))

