import os
import shutil
import glob
from random import shuffle, randint, choice


# image_path_easy = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split/images_easy"
image_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split/images"
image_path_hard = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split/images_hard"
label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split/labels"
image_path_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split_rotate/images"
label_path_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split_rotate/labels"
fold_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/folds"

def makeFolder(path_name,name):
    if not os.path.exists(os.path.join(path_name,name)):
        os.mkdir(os.path.join(path_name,name))
def createFolder(folder_path):
    for i in range(1,6):
        makeFolder(fold_path, "fold"+str(i))
        makeFolder(os.path.join(folder_path,"fold"+str(i)),"images")
        makeFolder(os.path.join(folder_path,"fold"+str(i),"images"), "train")
        makeFolder(os.path.join(folder_path,"fold"+str(i),"images"), "test_all")
        makeFolder(os.path.join(folder_path,"fold"+str(i),"images"), "test_rotate")
        makeFolder(os.path.join(folder_path,"fold"+str(i),"images"), "test_regular")
        makeFolder(os.path.join(folder_path,"fold"+str(i),"images"), "val")
        
        # makeFolder(os.path.join(fold_path,"fold"+str(i)),"labels")
        # makeFolder(os.path.join(fold_path,"fold"+str(i),"labels"), "train")
        # makeFolder(os.path.join(fold_path,"fold"+str(i),"labels"), "val")
        # makeFolder(os.path.join(fold_path,"fold"+str(i),"labels"), "test_all")
        # makeFolder(os.path.join(fold_path,"fold"+str(i),"labels"), "test_regular")
        # makeFolder(os.path.join(fold_path,"fold"+str(i),"labels"), "test_rotate")

dirs = os.listdir(image_path_hard)
shuffle(dirs)
j=0
i=0
for num in dirs:
    
    if i%6==0:
        j+=1
    name, ext = os.path.splitext(num)
    image_name = name+".jpg"
    label_name = name+".txt"
    image_name_rotate = name+"_rotate.jpg"
    label_name_rotate = name+"_rotate.txt"
    if j==1:
        crand = choice([True, False])
        if crand:
            shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(1),"images", "val"))
            shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(1),"labels", "val"))
        else:
            shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(1),"images", "val"))
            shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(1),"labels", "val"))
#==================copy to test path=================================#
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(1),"images", "test_all"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(1),"images", "test_regular"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(1),"images", "test_all"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(1),"images", "test_rotate"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(1),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(1),"labels", "test_regular"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(1),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(1),"labels", "test_rotate"))
#==================copy to train path ================================#
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(5),"images", "train"))
        
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(5),"labels", "train"))



    elif j==2:
        crand = choice([True, False])
        if crand:
            shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(2),"images", "val"))
            shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(2),"labels", "val"))
        else:
            shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(2),"images", "val"))
            shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(2),"labels", "val"))
#==================copy to test path=================================#
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(2),"images", "test_all"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(2),"images", "test_regular"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(2),"images", "test_all"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(2),"images", "test_rotate"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(2),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(2),"labels", "test_regular"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(2),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(2),"labels", "test_rotate"))
#==================copy to train path ================================#
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(5),"images", "train"))
        
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(5),"labels", "train"))

    elif j==3:
        crand = choice([True, False])
        if crand:
            shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(3),"images", "val"))
            shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(3),"labels", "val"))
        else:
            shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(3),"images", "val"))
            shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(3),"labels", "val"))
#==================copy to test path=================================#
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(3),"images", "test_all"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(3),"images", "test_regular"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(3),"images", "test_all"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(3),"images", "test_rotate"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(3),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(3),"labels", "test_regular"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(3),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(3),"labels", "test_rotate"))
#==================copy to train path ================================#
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(5),"images", "train"))
        
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(5),"labels", "train"))

    elif j==4:
        crand = choice([True, False])
        if crand:
            shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(4),"images", "val"))
            shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(4),"labels", "val"))
        else:
            shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(4),"images", "val"))
            shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(4),"labels", "val"))
#==================copy to test path=================================#
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(4),"images", "test_all"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(4),"images", "test_regular"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(4),"images", "test_all"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(4),"images", "test_rotate"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(4),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(4),"labels", "test_regular"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(4),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(4),"labels", "test_rotate"))
#==================copy to train path ================================#
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(5),"images", "train"))
        
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(5),"labels", "train"))

        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(1),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(5),"images", "train"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(1),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(5),"labels", "train"))

    elif j==5:
        crand = choice([True, False])
        if crand:
            shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(5),"images", "val"))
            shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(5),"labels", "val"))
        else:
            shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(5),"images", "val"))
            shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(5),"labels", "val"))
#==================copy to test path=================================#
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(5),"images", "test_all"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(5),"images", "test_regular"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(5),"images", "test_all"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(5),"images", "test_rotate"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(5),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(5),"labels", "test_regular"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(5),"labels", "test_all"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(5),"labels", "test_rotate"))
#==================copy to train path ================================#
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path_rotate,image_name_rotate),os.path.join(fold_path,"fold"+str(1),"images", "train"))
        
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path_rotate,label_name_rotate),os.path.join(fold_path,"fold"+str(1),"labels", "train"))

        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(2),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(3),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(4),"images", "train"))
        shutil.copy2(os.path.join(image_path,image_name),os.path.join(fold_path,"fold"+str(1),"images", "train"))

        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(2),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(3),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(4),"labels", "train"))
        shutil.copy2(os.path.join(label_path,label_name),os.path.join(fold_path,"fold"+str(1),"labels", "train"))

    else:
        print("J out of bound")





    i+=1