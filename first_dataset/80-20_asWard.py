import os
import glob
import shutil

ward_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/wardHistAdj/wardHistAdj_80-20_trainEasy"

img_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60"

for img in glob.glob(os.path.join(ward_path,"images/train/*.png")):
    _,name = os.path.split(img)
    name_only = os.path.splitext(name)[0]
    name_60 = name_only+".jpg"
    if os.path.exists(os.path.join(img_path,"easy/images",name_60)):
        shutil.copy2(os.path.join(img_path,"easy/images",name_60), os.path.join(img_path, "60_80-20_trainEasy/images/train"))
    elif os.path.exists(os.path.join(img_path,"hard/images",name_60)):
        shutil.copy2(os.path.join(img_path,"hard/images",name_60), os.path.join(img_path, "60_80-20_trainEasy/images/train"))
    elif os.path.exists(os.path.join(img_path,"flip_hard/images",name_60)):
        shutil.copy2(os.path.join(img_path,"flip_hard/images",name_60), os.path.join(img_path, "60_80-20_trainEasy/images/train"))
    else:
        print("image not found")

for img in glob.glob(os.path.join(ward_path,"images/test/*.png")):
    _,name = os.path.split(img)
    name_only = os.path.splitext(name)[0]
    name_60 = name_only+".jpg"   
    if os.path.exists(os.path.join(img_path,"easy/images",name_60)):
        shutil.copy2(os.path.join(img_path,"easy/images",name_60), os.path.join(img_path, "60_80-20_trainEasy/images/test"))
    elif os.path.exists(os.path.join(img_path,"hard/images",name_60)):
        shutil.copy2(os.path.join(img_path,"hard/images",name_60), os.path.join(img_path, "60_80-20_trainEasy/images/test"))
    elif os.path.exists(os.path.join(img_path,"flip_hard/images",name_60)):
        shutil.copy2(os.path.join(img_path,"flip_hard/images",name_60), os.path.join(img_path, "60_80-20_trainEasy/images/test"))
    else:
        print("image not found")

