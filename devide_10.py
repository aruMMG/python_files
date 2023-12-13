import os
import shutil
import glob
import random
from utils import makeFolder

image_all = glob.glob("/home/aru/run4/time1/images/*.exr")
label_path = "/home/aru/run4/time1/labels"
src_folder = "/home/aru/run4/time1/images"
base_folder = "/home/aru/run4"
makeFolder(base_folder, "time1_separate_10")
dst_folder = os.path.join(base_folder, "time1_separate_10")

for i in range(1,9):
    assert len(image_all)+(i-1)*10==80, "some miscalculation"
    makeFolder(dst_folder, str(i))
    dst_separate_folder = os.path.join(dst_folder, str(i), "images")
    dst_separate_folder_label = os.path.join(dst_folder, str(i), "labels")
    makeFolder(os.path.join(dst_folder, str(i)), "images")
    makeFolder(os.path.join(dst_folder, str(i)), "labels")
    selected_image = random.sample(image_all, 10)
    assert len(selected_image)==10, "10 images not selected"
    for img in selected_image:
        img_name = os.path.basename(img)
        only_name = img_name.split(".")[0]
        
        label_name = only_name+".txt"
        src_label_path = os.path.join(label_path, label_name)
        dst_label_path = os.path.join(dst_separate_folder_label, label_name)

        shutil.copy2(img, os.path.join(dst_separate_folder, img_name))
        shutil.copy2(src_label_path, dst_label_path)
        image_all.remove(img)
