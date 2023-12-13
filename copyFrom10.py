import os
import shutil
import glob

path_10 = "/home/aru/yolov5_hdr/datasets/10_real_10_synth"
path_80 = "/home/aru/yolov5_hdr/datasets/80_real_10_synth"

for fold in range(1,6):
    src_dir_img = os.path.join(path_10, "fold"+str(fold), "images/train")
    dst_dir_img = os.path.join(path_80, "fold"+str(fold), "images/train")
    src_dir_lab = os.path.join(path_10, "fold"+str(fold), "labels/train")
    dst_dir_lab = os.path.join(path_80, "fold"+str(fold), "labels/train")

    for img in glob.glob(os.path.join(src_dir_img, "*.exr")):
        img_name = os.path.basename(img)
        if img_name.startswith("img_obj") or img_name.startswith("r4"):
            shutil.copy2(img, os.path.join(dst_dir_img, img_name))
            lab_name = img_name.split(".")[0] + "txt"
            shutil.copy2(os.path.join(src_dir_lab, lab_name), os.path.join(dst_dir_lab, lab_name))
