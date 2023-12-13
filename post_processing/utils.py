import cv2
import numpy as np
import matplotlib.pyplot as plt


def box_iou(boxA, boxB):
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)
	# return the intersection over union value
	return iou


# img = cv2.imread("/home/aru/phd/objective1/hdr/python/lc3/rm_bg/img38_125.png", cv2.IMREAD_GRAYSCALE)
# print(img.shape)
# vals = img.flatten()
# print(vals.shape)
# counts, bins = np.histogram(vals, range(257))
# counts = np.delete(counts, [0])
# bins = np.delete(bins, [0])

# # plot histogram centered on values 0..255
# plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
# plt.xlim([-5, 255.5])
# plt.savefig("/home/aru/phd/objective1/hdr/python/lc3/histogram/paper/img38_125.png")