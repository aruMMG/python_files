import os
import shutil
import glob
import re

image_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/reinhard_gamma_CC/1024/split/images"
# label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split/labels"
image_path_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/reinhard_gamma_CC/1024/split_rotate/images"
# label_path_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split_rotate/labels"
path_hard = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split/images_hard"
fold_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/reinhard_gamma_CC/1024/folds"

path_60 = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/hardRotate_lc1_60_folds"
def makeFolder(path_name,name):
    if not os.path.exists(os.path.join(path_name,name)):
        os.mkdir(os.path.join(path_name,name))

for i in range(1,6):
    makeFolder(fold_path, "fold"+str(i))
    makeFolder(os.path.join(fold_path,"fold"+str(i)),"images")
    makeFolder(os.path.join(fold_path,"fold"+str(i),"images"), "train")
    makeFolder(os.path.join(fold_path,"fold"+str(i),"images"), "test_all")
    makeFolder(os.path.join(fold_path,"fold"+str(i),"images"), "test_rotate")
    makeFolder(os.path.join(fold_path,"fold"+str(i),"images"), "test_regular")
    makeFolder(os.path.join(fold_path,"fold"+str(i),"images"), "val")


j=0
while j<5:
    j+=1
    label_path = os.path.join(path_60, "fold"+str(j), "labels")
    label_save_path = os.path.join(fold_path,"fold"+str(j),"labels")
    shutil.copytree(label_path,label_save_path)

    image_path_60 = os.path.join(path_60, "fold"+str(j),"images/val","*.jpg")

    for img in glob.glob(image_path_60):
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]
        image_num = re.search(r"\d+", name_only)
        image_name = name_only+".png"
        if os.path.exists(os.path.join(image_path,image_name)):
            full_image_path = os.path.join(image_path, image_name)
            reverse_image_name = name_only+"_rotate.png"
            reverse_image_path = os.path.join(image_path_rotate,reverse_image_name)
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "val"))
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_regular"))
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_all"))
            shutil.copy2(reverse_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_all"))
            shutil.copy2(reverse_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_rotate"))

            for num in range(1,6):
                if j==num:
                    continue
                shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))
                if os.path.exists(os.path.join(path_hard,name_with_ext)):
                    shutil.copy2(reverse_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))



        elif os.path.exists(os.path.join(image_path_rotate,image_name)):
            reverse_image_name = "img"+image_num.group()+".png"
            reverse_image_name_60 = "img"+image_num.group()+".jpg"
            reverse_image_path = os.path.join(image_path,reverse_image_name)
            full_image_path = os.path.join(image_path_rotate, image_name)
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "val"))
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_rotate"))
            shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_all"))
            shutil.copy2(reverse_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_all"))
            shutil.copy2(reverse_image_path, os.path.join(fold_path,"fold"+str(j),"images", "test_regular"))

            for num in range(1,6):
                if j==num:
                    continue
                shutil.copy2(full_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))
                if os.path.exists(os.path.join(path_hard,reverse_image_name_60)):
                    shutil.copy2(reverse_image_path, os.path.join(fold_path,"fold"+str(num),"images", "train"))
            
        else:
            print("image not available")

        