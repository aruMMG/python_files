import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np

mAP50_0, mAP50_10, mAP50_20, mAP50_40, mAP50_80,mAP_0, mAP_10, mAP_20, mAP_40, mAP_80 = [],[], [], [], [], [], [], [], [], []
dict50 = {}
with open("/home/sakuni/phd/results/p2/test/all/mAP.csv", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line_lis = line.split(",")
        if i<2:
            continue
        elif i<7:
            mAP_10.append(float(line_lis[-1]))
            mAP50_10.append(float(line_lis[-3]))
        elif i<12:           
            mAP_20.append(float(line_lis[-1]))
            mAP50_20.append(float(line_lis[-3]))
        elif i<17:           
            mAP_40.append(float(line_lis[-1]))
            mAP50_40.append(float(line_lis[-3]))
        elif i<22:           
            mAP_80.append(float(line_lis[-1]))
            mAP50_80.append(float(line_lis[-3]))


# fig = plt.figure(figsize=(3.6,3.6), dpi=600)
# ax = fig.add_subplot()
plt.figure(figsize=(2,7), dpi=600)
plt.ylim(0,15)
plt.xlim(0,10)

base = [0,0]
# ax.set_yticks(np.arange(.8,1.1,0.1))
rect = Rectangle((0,0), 8.53, 1,color="teal")
plt.gca().add_patch(rect)
rect = Rectangle((0,1), 8.53, 6.4, color="teal")
plt.gca().add_patch(rect)
rect = Rectangle((0,1), 8.53, 6.4, color="blue",fill=False, hatch="|", linewidth=0.0)
plt.gca().add_patch(rect)

rect = Rectangle((0,6.4), 8.53, 1.9, color="green")
plt.gca().add_patch(rect)
rect = Rectangle((0,8.3), 8.53, 1.3, color="green")
plt.gca().add_patch(rect)
rect = Rectangle((0,8.3), 8.53, 1.3, color="blue",fill=False, hatch="|", linewidth=0.0)
plt.gca().add_patch(rect)

rect = Rectangle((0,9.6), 8.53, 1.6, color="orange")
plt.gca().add_patch(rect)

rect = Rectangle((0,11.2), 8.53, 0.9, color="red")
plt.gca().add_patch(rect)


rect = Rectangle((0,12.1), 4.265, 0.3, color="orange")
plt.gca().add_patch(rect)
rect = Rectangle((0,12.1), 4.265, 0.3, color="blue",fill=False, hatch="///", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((4.265,12.1), 4.265, 0.3, color="red")
plt.gca().add_patch(rect)
rect = Rectangle((4.265,12.1), 4.265, 0.3, color="blue",fill=False, hatch="///", linewidth=0.0)
plt.gca().add_patch(rect)


plt.tight_layout()

plt.savefig('plots/plotcircles1.png')