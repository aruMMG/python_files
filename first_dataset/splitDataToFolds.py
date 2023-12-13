import os
import glob
import shutil
from random import shuffle
import cv2

image_path = glob.glob("/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/hard/images/*.jpg")
shuffle(image_path)
image_path_flip = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/hard/flip_images"
label_path1 = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/hard/labels"
label_path_flip = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/hard/flip_labels"
#label_path2 = "/home/sakuni/phd/Experiments/hdr/dataset/hard/labels_seen_in_any_exposure/labels_double"
img_in_fold = int(len(image_path)/5)
fold_path = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/60/folds"


i=0
j=0
for img in image_path:
    
    img_path, name = os.path.split(img)
    name_only = os.path.splitext(name)[0]
    print(name_only)
    label_name = name_only+".txt"
    label_file_path = os.path.join(label_path1, label_name)
    assert os.path.exists(label_file_path), "Label file not exist"

    if image_path_flip and label_path_flip:
        img_flip = os.path.join(image_path_flip,name_only+"_flip.jpg")
        assert os.path.exists(img_flip), "flip image file not exist"
        flip_label_name = name_only+"_flip.txt"
        flip_label_file_path = os.path.join(label_path_flip, flip_label_name)
        assert os.path.exists(flip_label_file_path), "filp label file not exist"
    else:
        flip_label_file_path = False
        img_flip = False

    #if os.path.exists(os.path.join(label_path1,label_name)):
    #    label_file_path = os.path.join(label_path1,label_name)
    #elif os.path.exists(os.path.join(label_path2,label_name)):
    #    label_file_path = os.path.join(label_path2,label_name)
    #else:
    #    print("label not found for {}", format(label_name))
    
    if i%img_in_fold==0:
        j+=1


    if j==1:    
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(1),"images", "val"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(5),"images", "train"))
        
        if flip_label_file_path and img_flip:
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(2),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(3),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(4),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        if flip_label_file_path and img_flip:
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

    elif j==2:    
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(2),"images", "val"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(5),"images", "train"))

        if flip_label_file_path and img_flip:
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(1),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(3),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(4),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        if flip_label_file_path and img_flip:
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

    elif j==3:    
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(3),"images", "val"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(5),"images", "train"))
        
        if flip_label_file_path and img_flip:
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(2),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(1),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(4),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        if flip_label_file_path and img_flip:
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

    elif j==4:    
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(4),"images", "val"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(5),"images", "train"))
        
        if flip_label_file_path and img_flip:
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(2),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(3),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(1),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "val"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        if flip_label_file_path and img_flip:
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "train"))

    elif j==5:    
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(img,os.path.join(fold_path,"fold"+str(5),"images", "val"))
        
        if flip_label_file_path and img_flip:
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(2),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(3),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(4),"images", "train"))
            shutil.copy2(img_flip,os.path.join(fold_path,"fold"+str(1),"images", "train"))

        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(label_file_path,os.path.join(fold_path,"fold"+str(5),"labels", "val"))

        if flip_label_file_path and img_flip:
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(2),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(3),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(4),"labels", "train"))
            shutil.copy2(flip_label_file_path,os.path.join(fold_path,"fold"+str(1),"labels", "train"))

    i+=1