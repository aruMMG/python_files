import os
import shutil
import glob
import re

fold_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/folds"

path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/single_exp/30/1024/fold"
img_hard = os.listdir(os.path.join(path,"hard"))

j=0
while j<5:
    j+=1
    label_path = os.path.join(fold_path, "fold"+str(j), "labels/val")

    image_path = os.path.join(fold_path, "fold"+str(j),"images/val","*.png")
    if not os.path.exists(os.path.join(fold_path,"fold"+str(j),"images", "test_hard")):
        os.mkdir(os.path.join(fold_path,"fold"+str(j),"images", "test_hard"))
    if not os.path.exists(os.path.join(fold_path,"fold"+str(j),"images", "test_easy")):
        os.mkdir(os.path.join(fold_path,"fold"+str(j),"images", "test_easy"))
    # if not os.path.exists(os.path.join(fold_path,"fold"+str(j),"labels", "test_hard")):
    #     os.mkdir(os.path.join(fold_path,"fold"+str(j),"labels", "test_hard"))
    # if not os.path.exists(os.path.join(fold_path,"fold"+str(j),"labels", "test_easy")):
    #     os.mkdir(os.path.join(fold_path,"fold"+str(j),"labels", "test_easy"))
    for img in glob.glob(image_path):
        copy = False
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]
        label_name = name_only+".txt"
        image_num = re.search(r"\d+", name_only)
        image_name = name_only+".jpg"
        if image_name in img_hard:
            copy = True
        

        if copy:
            shutil.copy2(img, os.path.join(fold_path,"fold"+str(j),"images", "test_hard"))
            # shutil.copy2(os.path.join(label_path,label_name), os.path.join(fold_path,"fold"+str(j),"labels", "test_hard"))
        else:
            # shutil.copy2(os.path.join(label_path,label_name), os.path.join(fold_path,"fold"+str(j),"labels", "test_easy"))
            shutil.copy2(img, os.path.join(fold_path,"fold"+str(j),"images", "test_easy"))
        

