import cv2
import os
import glob

image_path_flip = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/wardHistAdj/flip_hard"
image_path = glob.glob("/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/wardHistAdj/hard/*.png")
#label_path1 = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/reinhardLocal_gamma_CC/easy/labels"
#label_path_flip = "/home/sakuni/phd/Experiments/hdr/dataset/dataset_paper/reinhardLocal_gamma_CC/easy/flip_labels"


for img in image_path:

    img_path, name = os.path.split(img)
    name_only = os.path.splitext(name)[0]
    #label_name = name_only+".txt"
    #if os.path.exists(os.path.join(label_path1,label_name)):
    #    label_file_path = os.path.join(label_path1,label_name)
    #elif os.path.exists(os.path.join(label_path2,label_name)):
    #    label_file_path = os.path.join(label_path2,label_name)
    #else:
    #    print("label not found for {}", format(label_name))


    im = cv2.imread(img)
    flip_img = cv2.flip(im,0)

    cv2.imwrite(os.path.join(image_path_flip, name_only+"_flip.png"),flip_img)
"""
    with open(os.path.join(label_path1,label_name), "r") as f:

        with open(os.path.join(label_path_flip,name_only+"_flip.txt"), "w+") as f1:
            for line in f:
                print(line)
                lis = list(map(float, str.split(line)))
                lis[0] = int(lis[0])
                lis[2] = int(1024-lis[2]*1024)/1024
                f1.write(" ".join(str(item) for item in lis))
                f1.write("\n")
"""