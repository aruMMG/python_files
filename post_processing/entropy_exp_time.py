import matplotlib.pyplot as plt
import numpy as np
import cv2
import skimage.measure as measure
import glob
import os

def txt2labelarray(txtFile, size=1024):
    true_boxes = []

    with open(txtFile) as f:
        for cnt, line in enumerate(f):
            c,x,y,w,h = map(float, line.split())
            x = x*size
            y = y*size
            w = w*size
            h = h*size
            x1 = x - w/2
            x2 = x + w/2
            y1 = y - h/2
            y2 = y + h/2
            lis_for_each_sample = []
            lis_for_each_sample.append(0)
            lis_for_each_sample.append(x1)
            lis_for_each_sample.append(y1)
            lis_for_each_sample.append(x2)
            lis_for_each_sample.append(y2)
            
            true_boxes.append(lis_for_each_sample)
        labels = np.asarray(true_boxes)
    return labels


def entropy_image(image, exp_time, labels=False, whole_img=True):
    entropys = [exp_time]
    if whole_img:
        entropy = measure.shannon_entropy(image)
        entropys.append(entropy)
    if labels:
        for idx in range(labels.shape[0]):
            label = labels[idx]
            image_crop = image[int(label[2]):int(label[4]), int(label[1]):int(label[3]),:]
            # cv2.imwrite(str(exp_time)+".png", image_crop)
            entropy = measure.shannon_entropy(image_crop)
            entropys.append(entropy)
    
    return entropys

def entropy_split(image, labels):
    entropys = []
    for idx in range(labels.shape[0]):
        label = labels[idx]
        image_crop = image[int(label[2]):int(label[4]), int(label[1]):int(label[3]),:]
        # cv2.imwrite(str(exp_time)+".png", image_crop)
        entropy = measure.shannon_entropy(image_crop)
        entropys.append(entropy)

    return entropys

def entropy_images(image, exp_time, labels=False):
    entropy = measure.shannon_entropy(image)

    return entropy

def plot_entropys(entropy_arr):
    fig,ax = plt.subplots()
    color_list = ["r", "g", "b"]
    for idx in range(entropy_arr.shape[1]-1):
        ax.plot(np.log2(entropy_arr[:,0]/15), entropy_arr[:,idx+1], color_list[idx])
    fig.savefig("entropys_img.png")

def plot_entropys_rows(entropy_arr, entropy_arr2=False):
    fig,ax = plt.subplots()
    for idx in range(entropy_arr.shape[0]-1):
        ax.plot(np.log2(entropy_arr[0,:]/15), entropy_arr[idx+1,:], "b")
    
    if entropy_arr2.shape:
        for idx in range(entropy_arr2.shape[0]-1):
            ax.plot(np.log2(entropy_arr[0,:]/15), entropy_arr2[idx+1,:], "g")
        
    fig.savefig("entropys_imgs_labels.png")

if __name__=="__main__":
    exp_time_list = [15, 30, 60, 125, 250, 500, 1000, 2000, 4000]
    # entropy_list = [exp_time_list]

# ======================================One image plot============================================
    image_path1 = "/home/aru/phd/objective2/dataset/single_exp/"
    image_path2 = "/1024/split/images/img62.jpg"
    # label_path = "/home/aru/phd/objective2/dataset/single_exp/60/1024/split/labels/img62.txt"
    # labels = txt2labelarray(label_path)
    # for exp_time in exp_time_list:
    #     image_path = image_path1 + str(exp_time) + image_path2
    #     image = cv2.imread(image_path)
    #     entropys = entropy_image(image, exp_time, labels=labels)
        # entropy_list.append(entropys)

    # label_paths = "/home/aru/phd/objective2/dataset/single_exp/60/1024/split/labels"

# ==========================Whole image entropy for all images======================================

    image_path2 = "/1024/split/images/"

    # for image_path in glob.glob("/home/aru/phd/objective2/dataset/single_exp/60/1024/split/images/*.jpg"):
    #     image_name = os.path.basename(image_path)
    #     entropys_per_image = []
    #     for exp_time in exp_time_list:
    #         image_path = image_path1 + str(exp_time) + image_path2 + image_name
    #         image = cv2.imread(image_path)
    #         entropys = entropy_images(image, exp_time)
    #         entropys_per_image.append(entropys)
    #     entropy_list.append(entropys_per_image)
    
    # entropys_arr = np.array(entropy_list)
    # plot_entropys_rows(entropys_arr)

# =====================================Labels for all image============================================
    # entropy_list2 = [exp_time_list]
    # label_paths = "/home/aru/phd/objective2/dataset/single_exp/60/1024/split/labels"
    # for image_path in glob.glob("/home/aru/phd/objective2/dataset/single_exp/60/1024/split/images/*.jpg"):
    #     image_name = os.path.basename(image_path)
        
    #     label_name = image_name.split(".")[0]+".txt"
    #     label_path = os.path.join(label_paths, label_name)
    #     labels = txt2labelarray(label_path)

    #     entropys_per_image = []
    #     entropys_per_image2 = []
    #     for exp_time in exp_time_list:
    #         image_path = image_path1 + str(exp_time) + image_path2 + image_name
    #         image = cv2.imread(image_path)
    #         entropys = entropy_split(image,labels=labels)
    #         if len(entropys)>1:
    #             entropys_per_image2.append(entropys[1]) 
    #         entropys_per_image.append(entropys[0])
    #     entropy_list.append(entropys_per_image)
    #     if len(entropys_per_image2)>0:
    #         entropy_list2.append(entropys_per_image2)
    
    # entropys_arr = np.array(entropy_list)
    # entropys_arr2 = np.array(entropy_list2)
    # plot_entropys_rows(entropys_arr, entropys_arr2)

    # ================================Flat pbrt===========================================
    entropy_list = []
    label_path = "/home/aru/phd/objective2/paper_review/images/straight/47/pbrt/3b.txt"
    label = txt2labelarray(label_path, 700)
    imgs_path = "/home/aru/phd/objective2/paper_review/images/straight/15/pbrt"
    names = ["30m", "300m", "3b", "30b", "300b"]
    for idx, img_name in enumerate(names):
        img_path = imgs_path +"/"+ img_name + ".png"
        img = cv2.imread(img_path)
        print(img.shape)
        entropy = entropy_split(img, label)
        entropy_list.append([idx+1, entropy[0]])
    entropy_arr = np.array(entropy_list)
    print(entropy_arr)
    print(entropy_arr.shape)
    print(entropy_arr[:,0])
    plt.plot(entropy_arr[:,0], entropy_arr[:,1])
    plt.savefig("flat_entropy15.png")