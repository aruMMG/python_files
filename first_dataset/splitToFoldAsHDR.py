import os
import glob
import shutil
import re

path_hdr = "/home/sakuni/phd/Experiments/hdr/dataset/hard/60/folds"
image_path = "/home/sakuni/phd/Experiments/hdr/dataset/hard/gamma/reinhardLocal"

j=0
while j<5:
    j+=1
    path = os.path.join(path_hdr,"fold"+str(j))
    exr_path = os.path.join(path,"images/val/*.jpg")
    label_path = os.path.join(path,"labels/val")
    
    for img in glob.glob(exr_path):
        _, name_with_ext = os.path.split(img)
        print(name_with_ext)
        name = os.path.splitext(name_with_ext)[0]
        save_img_name = name+".png"
        save_label_name = name+".txt"
        """
        if name.startswith("hdr"):
            num = re.search(r"\d+", name)
            save_img_name = "img"+num.group()+".jpg"
            save_label_name = "img"+num.group()+".txt"
        elif name.startswith("img"):
            save_img_name = name+".jpg"
            save_label_name = name+".txt"

        else:
            print("Extra image found")
        """
        shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(j),"images", "val"))
        shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(j),"labels", "val",save_label_name))

        if j==1:
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(2),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(3),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(4),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(5),"images", "train"))
    
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(2),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(3),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(4),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(5),"labels", "train",save_label_name))

        elif j==2:
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(1),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(3),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(4),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(5),"images", "train"))
    
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(1),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(3),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(4),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(5),"labels", "train",save_label_name))

        elif j==3:
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(2),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(1),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(4),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(5),"images", "train"))
    
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(2),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(1),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(4),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(5),"labels", "train",save_label_name))
            
        elif j==4:    
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(2),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(3),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(1),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(5),"images", "train"))
    
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(2),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(3),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(1),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(5),"labels", "train",save_label_name))
        elif j==5:
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(2),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(3),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(4),"images", "train"))
            shutil.copy2(os.path.join(image_path,"fold",save_img_name),os.path.join(image_path,"folds","fold"+str(1),"images", "train"))
    
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(2),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(3),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(4),"labels", "train",save_label_name))
            shutil.copy2(os.path.join(label_path,name+".txt"),os.path.join(image_path,"folds","fold"+str(1),"labels", "train",save_label_name))
        else:
            print("j greater than 5")
    print(j)