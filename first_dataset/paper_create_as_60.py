import os
import shutil
import glob
import re

path_exr = "/home/sakuni/phd/Experiments/hdr/data_capture/data2/Session1/1024/all/exr"
path_60 = '/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/hard/*.jpg'
paper_path = '/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/exr/hard'

for img in glob.glob(path_60):
    _,name_with_ext = os.path.split(img)
    img_name = os.path.splitext(name_with_ext)[0]
    print(img_name)
    if img_name.startswith("img_cali"):
        image_name = img_name+".exr"
    elif img_name.startswith("img"):
        num = re.search(r"\d+", img_name)
        image_name = "hdr"+num.group()+".exr"
    else:
        print("Different image found {}", format(img_name))

    shutil.copy2(os.path.join(path_exr,image_name), paper_path)
    