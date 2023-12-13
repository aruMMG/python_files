import cv2
import numpy as np
import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"


# img1 = cv2.imread("/home/aru/phd/objective2/pbrt-v3/scenes/nakajima/images/Al_smooth_scaled_5.5_4096.exr", flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)

# tonemap = cv2.createTonemap()
# img = tonemap.process(img1)
# cv2.imwrite("/home/aru/phd/objective2/pbrt-v3/scenes/nakajima/images/Al_smooth_scaled_5.5_4096.png", img*255)


img_path = "/home/aru/phd/objective2/dataset/images/big/img91.exr"
img = cv2.imread(img_path, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
maximum = np.max(img)
img/=maximum
ton_img = img**(1/4.2)
img_name = os.path.basename(img_path)
img_name = os.path.splitext(img_name)[0]+'.jpg'
# print(img_name)
# tonemap1 = cv2.createTonemapMantiuk(2.2)
# ton_img = tonemap1.process(img.copy())
tone_img = np.clip(ton_img*255,0,255).astype('uint8')
cv2.imwrite(os.path.join("/home/aru/", img_name), tone_img)