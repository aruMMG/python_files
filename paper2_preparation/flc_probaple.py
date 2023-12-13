import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
def objective(x, a=20): # 60 - 2.5, 40 - 17, 100 - 10, 80 - 0, 120 - 10, 140 - 10, full - 5 For 40 and 60 the addefect file is changed
    if x>0:
        return int(a+0.6*x)
    else:
        return int(a+0.5*abs(x))
    

def visualize_results(results_path, img_size = (1024, 1024, 3)):
    cnt = 0

    tl = 3
    tf = 2
    w=img_size[0]
    h=img_size[1]

    mosaic = np.full(img_size, 200, dtype=np.uint8)
    c=0
    for i in range(300, 824):
        x = i-512
        y = objective(x)
        c+=1
        for j in range(40):
            mosaic[300+y+j,i,:] = (127-j*3, 127-j*3, 127-j*3)
            if c==1:
                print(127-j*3)
            
    Image.fromarray(mosaic).save(os.path.join(results_path, "flc.png"))




if __name__=="__main__":
    results_path = "/home/aru"
    conf_thres = 0.25
    img_size = 1024
    batch_size = 4
    visualize_results(results_path)