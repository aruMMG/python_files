import os
import shutil
import glob
from random import shuffle, randint, choice


image_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/reinhard_gamma_CC/1024/split/images"
label_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split/labels"
image_path_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/reinhard_gamma_CC/1024/split_rotate/images"
label_path_rotate = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/single_exp/60/1024/split_rotate/labels"
fold_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc1/tonemaped/reinhard_gamma_CC/1024/folds"

i=0
j=0
lis = list(range(1,111))
lis[18] = 111
lis[21] = 112
lis[16] = 113
shuffle(lis)
print(lis)
for num in lis:
    
    if i%22==0:
        j+=1
    
    image_name = "img"+str(num)+".png"
    label_name = "img"+str(num)+".txt"
    image_name_rotate = "img"+str(num)+"_rotate.png"
    label_name_rotate = "img"+str(num)+"_rotate.txt"
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