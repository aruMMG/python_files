import os
import glob
import shutil

path = "/home/aru/phd/hdr/dataset/dataset1"


image_path = os.path.join(path,"image")
label_path = os.path.join(path,"label")
path=os.path.join(path,"5fold")
i=0
j=0
print(len(glob.glob(os.path.join(image_path,"*.exr"))))
for img in glob.glob(os.path.join(image_path,"*.exr")):
    img_path, name = os.path.split(img)
    label_name = os.path.splitext(name)[0]
    label_file_path = os.path.join(label_path,label_name+".txt")
    if i%22==0:
        j+=1


    if j==1:    
        shutil.copy2(img,os.path.join(path,"fold"+str(1),"images", "val"))
        shutil.copy2(img,os.path.join(path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(1),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(5),"labels", "train"))

    elif j==2:    
        shutil.copy2(img,os.path.join(path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(2),"images", "val"))
        shutil.copy2(img,os.path.join(path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(2),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(5),"labels", "train"))

    elif j==3:    
        shutil.copy2(img,os.path.join(path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(3),"images", "val"))
        shutil.copy2(img,os.path.join(path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(3),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(5),"labels", "train"))

    elif j==4:    
        shutil.copy2(img,os.path.join(path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(4),"images", "val"))
        shutil.copy2(img,os.path.join(path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(4),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(5),"labels", "train"))

    elif j==5:    
        shutil.copy2(img,os.path.join(path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(path,"fold"+str(5),"images", "val"))

        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(path,"fold"+str(5),"labels", "val"))
    i+=1
