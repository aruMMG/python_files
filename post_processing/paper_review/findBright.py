import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("/home/aru/phd/objective2/dataset/single_exp/30/1024/split_rotate/images/img64_rotate.jpg")
# img = cv2.imread("rembg.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Y = xyz_img[:,:,1]
vec = img.reshape((-1,3))
vec = np.float32(vec)
print(vec.shape)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
attempts=10
ret,label,center=cv2.kmeans(vec,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
print(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))

print("label:{}".format(np.unique(label)))
print(label.shape)
print(np.unique(res))
print(result_image.shape)
figure_size = 15
plt.figure(figsize=(figure_size,figure_size))
plt.subplot(1,2,1),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(result_image)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])
plt.savefig("segmentation.png")