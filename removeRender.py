import glob
import os
from utils import makeFolder
import shutil

save_path = "/home/aru/yolov5_hdr/datasets/80_real/fold5/labels/train"
for img in glob.glob("/home/aru/yolov5_hdr/datasets/80_real_80_random_synth_folds/fold5/labels/train/*.txt"):
    img_name = os.path.basename(img)
    if img_name.startswith("img_obj"):
        continue
    else:
        shutil.copy2(img, os.path.join(save_path, img_name))
