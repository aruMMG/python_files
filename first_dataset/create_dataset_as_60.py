import os
import glob
import shutil
import re

path_60 = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/fold/*.jpg"
image_path_easy = "/home/sakuni/phd/Experiments/hdr/dataset/hard/gamma/WardHistAdj/double"
image_path_hard = "/home/sakuni/phd/Experiments/hdr/dataset/hard/gamma/WardHistAdj/set1"
p,_ = os.path.split(image_path_set)
if not os.path.exists(os.path.join(p,"fold")):
    os.mkdir(os.path.join(p,"fold"))
image_path_fold = "/home/sakuni/phd/Experiments/hdr/dataset/hard/gamma/WardHistAdj/fold"

for img in glob.glob(path_60):
    _,name_with_ext = os.path.split(img)
    img_name = os.path.splitext(name_with_ext)[0]
    if img_name.startswith("img_cali"):
        image_name = img_name+".png"
        image_save_name = image_name
    elif img_name.startswith("img"):
        num = re.search(r"\d+", img_name)
        image_name = "hdr"+num.group()+".png"
        image_save_name = "img"+num.group()+".png"
    else:
        print("Different image found {}", format(img_name))

    if os.path.exists(os.path.join(image_path_double,image_name)):
        shutil.copy2(os.path.join(image_path_double,image_name),os.path.join(image_path_fold, image_save_name))
    elif os.path.exists(os.path.join(image_path_set,image_name)):
        shutil.copy2(os.path.join(image_path_set,image_name),os.path.join(image_path_fold,image_save_name))
    else:
        print("image not found {}", format(image_name))
        
