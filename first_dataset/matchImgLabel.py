import os
import shutil
import glob
import re

image_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/wardHistAdj/flip_hard"
label_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/hard/flip_labels"

shutil.copytree(label_path, os.path.join(image_path,"labels"))

for img in glob.glob(os.path.join(image_path,"*.png")):
    _,name_with_ext = os.path.split(img)
    name_only = os.path.splitext(name_with_ext)[0]
    if name_only.startswith("img_cali"):
        shutil.copy2(img,os.path.join(image_path,"images"))
    elif name_only.startswith("hdr"):
        num = re.search(r"\d+", name_only)
        image_name = "img" + num.group() + "_flip.png"
        shutil.copy2(img,os.path.join(image_path,"images",image_name))
