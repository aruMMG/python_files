from rembg import remove
import cv2
import numpy as np
def remove_bg(file_path, save_path):
    img = cv2.imread(file_path)
    out_img = remove(img)
    cv2.imwrite(save_path, out_img)

def rm_bg_img(ref_img_path, file_path, save_path):
    img = cv2.imread(ref_img_path)
    img_to_rm_bg = cv2.imread(file_path)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.array_equal(img[i,j,:], np.array([0,0,0])):
                img_to_rm_bg[i,j,:] = (0,0,0)
    cv2.imwrite(save_path, img_to_rm_bg)

if __name__=="__main__":
    file_path = "/home/aru/phd/objective2/dataset/single_exp/500/1024/split/images/img38.jpg"
    save_path = "/home/aru/phd/objective1/hdr/python/lc3/rm_bg/img38_500.png"
    
    # Remove background using rembg
    remove_bg(file_path, save_path)

    # remove background based on other image
    ref_img_path = "/home/aru/phd/objective1/hdr/python/lc3/rm_bg/img38_15.png"
    rm_bg_img(ref_img_path, file_path, save_path)