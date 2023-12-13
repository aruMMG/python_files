import glob
import os
import csv
fold_dir = "/home/aru/detection_models/fasterrcnn-pytorch-training-pipeline/wardHistAdj"

for i in range(5):
    name_list = []
    fold = i+1
    fold_path = os.path.join(fold_dir, "fold"+str(fold))
    for img in glob.glob(os.path.join(fold_path, "images/train/*.png")):
        name = os.path.basename(img).split(".")[0]
        name_list.append(name)

    if os.path.exists(os.path.join(fold_path, "images/val")):
        name_list.append("val")
        for img in glob.glob(os.path.join(fold_path, "images/val/*.png")):
            name = os.path.basename(img).split(".")[0]
            name_list.append(name)
    with open(os.path.join(fold_dir, str(fold)+".csv"), "w") as f:
        wr = csv.writer(f)
        wr.writerow(name_list)
    
