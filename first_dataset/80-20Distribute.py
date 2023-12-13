import glob
import os
import shutil
from random import shuffle
source_path = glob.glob("/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/reinhardLocal_gamma_CC/easy/images/*.png")
label_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/reinhardLocal_gamma_CC/easy/labels"
shuffle(source_path)
total_img = len(source_path)
save_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/wardHistAdj/wardHistAdj_80-20_trainHard"

j=0
for img in source_path:
    j+=1
    _,name_with_ext = os.path.split(img)
    name_only = os.path.splitext(name_with_ext)[0]
    label_name = name_only+".txt"


    if j<=int(total_img/5):
        shutil.copy2(img, os.path.join(save_path,"images/train",name_with_ext))
        shutil.copy2(os.path.join(label_path,label_name), os.path.join(save_path,"labels/train", label_name))
    elif j>int(total_img/5):
        shutil.copy2(os.path.join(label_path,label_name), os.path.join(save_path,"labels/test", label_name))
        shutil.copy2(img, os.path.join(save_path,"images/test",name_with_ext))
    else:
        print("ERROR")
    

