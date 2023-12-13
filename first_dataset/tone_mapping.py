import cv2
import os
import glob
import path

path_exr = '/home/sakuni/phd/Experiments/hdr/dataset/hard/exr/set1/*.exr'
out_path = '/home/sakuni/phd/Experiments/hdr/dataset/hard'
for img in glob.glob(path_exr):
    _,name = os.path.split(img)
    hdr = cv2.imread(img, cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
    name = os.path.splitext(name)[0]

    out_path_reinhard = os.path.join(out_path, "reinhard/set1")
    tonemapReinhard = cv2.createTonemapReinhard(1.5, 0,0,0)
    ldrReinhard = tonemapReinhard.process(hdr)
    cv2.imwrite(os.path.join(out_path_reinhard,name+".png"), ldrReinhard * 255)

    out_path_mantiuk = os.path.join(out_path, "mantiuk/set1")
    tonemapMantiuk = cv2.createTonemapMantiuk(2.2,0.85, 1.2)
    ldrMantiuk = tonemapMantiuk.process(hdr)
    #ldrMantiuk = 3 * ldrMantiuk
    cv2.imwrite(os.path.join(out_path_mantiuk,name+".png"), ldrMantiuk * 255)
  
    """   
    out_path_linear = os.path.join(out_path, "linear/images_1024")
    ldrLinear = hdr/(hdr.max())
    cv2.imwrite(os.path.join(out_path_linear,name+".png"), ldrLinear * 255)
"""



