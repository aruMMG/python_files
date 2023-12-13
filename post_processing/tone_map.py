import numpy as np
import cv2
import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import glob

# save_path = "/home/aru/phd/objective2/dataset/compare/tone_map/gamma/4.2/fig4"
save_path = "/home/aru/run_p2"

for img_path in glob.glob("/home/aru/run_p2/*.exr"): 
# for img_path in glob.glob("/home/aru/phd/objective2/p2/image_bump/New Folder(1)/hdr_created/*.exr"): 
# img_path = "/home/aru/phd/objective2/dataset/images/small_rotate/img69_rotate.exr"
    img = cv2.imread(img_path, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
    maximum = np.max(img)
    # dev_nor = np.ceil(np.log2(maximum))
    img/=maximum
    ton_img = img**(1/5.2)
    img_name = os.path.basename(img_path)
    img_name = os.path.splitext(img_name)[0]+'.jpg'
    # print(img_name)
    # tonemap1 = cv2.createTonemapMantiuk(2.2)
    # ton_img = tonemap1.process(img.copy())
    tone_img = np.clip(ton_img*255,0,255).astype('uint8')
    cv2.imwrite(os.path.join(save_path, img_name), tone_img)