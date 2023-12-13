from glob import glob
import os
import random
import shutil
import glob
from utils import makeFolder

label_path1 = "/home/aru/yolov5_hdr/datasets/real_test_p1/hdr/fold1/labels/val"
label_path2 = "/home/aru/yolov5_hdr/datasets/real_test_p1/hdr/fold2/labels/val"
label_path3 = "/home/aru/yolov5_hdr/datasets/real_test_p1/hdr/fold3/labels/val"
label_path4 = "/home/aru/yolov5_hdr/datasets/real_test_p1/hdr/fold4/labels/val"
label_path5 = "/home/aru/yolov5_hdr/datasets/real_test_p1/hdr/fold5/labels/val"


big_img = glob.glob("/home/aru/phd/objective2/dataset/images/big/*.exr")
small_img = glob.glob("/home/aru/phd/objective2/dataset/images/small/*.exr")
small_rotate_img = glob.glob("/home/aru/phd/objective2/dataset/images/small_rotate/*.exr")
all_img_path = big_img + small_img + small_rotate_img

num = 40
folds_path = "/home/aru/yolov5_hdr/datasets/40_real"
val_paths = "/home/aru/yolov5_hdr/datasets/Real_test"

big = 7
if random.random()>0.5:
    big = 8

# fold1
for fold in range(1,6):

    fold_name =  "fold"+str(fold)
    val_path = glob.glob(os.path.join(val_paths, "fold"+str(fold), "images/val/*.exr"))
    val_imgs = [os.path.basename(x).split(".")[0] for x in val_path]
    img_to_select_from = []
    for img in all_img_path:
        name_only = os.path.basename(img).split(".")[0]
        if name_only in val_imgs:
            continue
        else:
            img_to_select_from.append(img)
    
    assert len(img_to_select_from) == 80, "80 image not available to select from"
    select_fold = random.sample(img_to_select_from, num)
    assert num==len(select_fold), "selected inage is not equal to {}".format(num)
    makeFolder(folds_path, fold_name)

    fold_path = os.path.join(folds_path, fold_name)
    makeFolder(fold_path, "images")
    makeFolder(fold_path, "labels")
    train_path_image = os.path.join(folds_path, fold_name, "images/train")
    train_path_label = os.path.join(folds_path, fold_name, "labels/train")
    makeFolder(fold_path, "images/train")
    makeFolder(fold_path, "labels/train")

    
    for img in select_fold:
        img_name = os.path.basename(img)
        name_only = img_name.split(".")[0]
        label_name = name_only + ".txt"
        shutil.copy2(img, os.path.join(train_path_image, img_name))

        if os.path.exists(os.path.join(label_path1, label_name)):
            shutil.copy2(os.path.join(label_path1, label_name), os.path.join(train_path_label, label_name))
        elif os.path.exists(os.path.join(label_path2, label_name)):
            shutil.copy2(os.path.join(label_path2, label_name), os.path.join(train_path_label, label_name))
        elif os.path.exists(os.path.join(label_path3, label_name)):
            shutil.copy2(os.path.join(label_path3, label_name), os.path.join(train_path_label, label_name))
        elif os.path.exists(os.path.join(label_path4, label_name)):
            shutil.copy2(os.path.join(label_path4, label_name), os.path.join(train_path_label, label_name))
        elif os.path.exists(os.path.join(label_path5, label_name)):
            shutil.copy2(os.path.join(label_path5, label_name), os.path.join(train_path_label, label_name))
        else:
            print("label not available")