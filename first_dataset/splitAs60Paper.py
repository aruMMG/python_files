import os
import glob
import shutil
import re

path_60 = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/60_folds"
img_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/wardHistAdj"


j=0
while j<5:
    j+=1
    label_path = os.path.join(path_60,"fold"+str(j),"labels")
    label_save_path = os.path.join(img_path,"folds","fold"+str(j),"labels")
    shutil.copytree(label_path,label_save_path)

    image_path_60 = os.path.join(path_60, "fold"+str(j),"images/val","*.jpg")
    for img in glob.glob(image_path_60):
        flip_image_path = False
        _,name_with_ext = os.path.split(img)
        name_only = os.path.splitext(name_with_ext)[0]
        print(name_only)
        if name_only.startswith("img_cali"):
            img_name = name_only+".png"
            img_save_name = name_only+".png"
            flip_img_name = name_only+"_flip.png"
            flip_img_save_name = name_only+"_flip.png"
            
            if os.path.exists(os.path.join(img_path,"easy",img_name)):
                image_path = os.path.join(img_path,"easy",img_name)
            elif os.path.exists(os.path.join(img_path,"hard",img_name)):
                image_path = os.path.join(img_path,"hard",img_name)
                flip_image_path = os.path.join(img_path,"flip_hard",flip_img_name)

        elif name_only.startswith("img"):
            num = re.search(r"\d+", name_only)
            img_name = "hdr"+num.group()+".png"
            img_save_name = "img"+num.group()+".png"
            flip_img_name = "hdr"+num.group()+"_flip.png"
            flip_img_save_name = "img"+num.group()+"_flip.png"

            if os.path.exists(os.path.join(img_path,"easy",img_name)):
                image_path = os.path.join(img_path,"easy",img_name)
            elif os.path.exists(os.path.join(img_path,"hard",img_name)):
                image_path = os.path.join(img_path,"hard",img_name)
                flip_image_path = os.path.join(img_path,"flip_hard",flip_img_name)
        else:
            print("image not exist")

        shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(j),"images", "val", img_save_name))
        

        if j==1:
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", img_save_name))
    
            if flip_image_path:
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", flip_img_save_name))               


        elif j==2:
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", img_save_name))
    
            if flip_image_path:
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", flip_img_save_name))               

        elif j==3:
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", img_save_name))
    
            if flip_image_path:
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", flip_img_save_name))               

        elif j==4:
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", img_save_name))
    
            if flip_image_path:
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(5),"images", "train", flip_img_save_name))               

        elif j==5:
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", img_save_name))
            shutil.copy2(image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", img_save_name))
    
            if flip_image_path:
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(2),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(3),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(4),"images", "train", flip_img_save_name))
                shutil.copy2(flip_image_path, os.path.join(img_path,"folds","fold"+str(1),"images", "train", flip_img_save_name))               

        else:
            print("J greater than 5")

