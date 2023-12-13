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
rect = Rectangle((0,1), 8.53, 3.8, color="teal")
plt.gca().add_patch(rect)
rect = Rectangle((0,1), 8.53, 3.8, color="blue",fill=False, hatch="///", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,4.8), 8.53, 0.2, color="teal")
plt.gca().add_patch(rect)
rect = Rectangle((0,4.8), 8.53, 0.2, color="blue",fill=False, hatch="xxx", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,5), 8.53, 0.5, color="teal")
plt.gca().add_patch(rect)
rect = Rectangle((0,5), 8.53, 0.5, color="blue",fill=False, hatch="|||", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,5.5), 8.53, 2.3, color="teal")
plt.gca().add_patch(rect)
rect = Rectangle((0,5.5), 8.53, 2.3, color="blue",fill=False, hatch="|", linewidth=0.0)
plt.gca().add_patch(rect)

rect = Rectangle((0,7.8), 8.53, 1.6, color="green")
plt.gca().add_patch(rect)
rect = Rectangle((0,7.8), 8.53, 1.6, color="blue",fill=False, hatch="|||", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,9.4), 8.53, 0.2, color="green")
plt.gca().add_patch(rect)
rect = Rectangle((0,9.4), 8.53, 0.2, color="blue",fill=False, hatch="xxx", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,9.6), 8.53, 0.1, color="green")
plt.gca().add_patch(rect)
rect = Rectangle((0,9.7), 8.53, 0.4, color="green")
plt.gca().add_patch(rect)
rect = Rectangle((0,9.7), 8.53, 0.4, color="blue",fill=False, hatch="///", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,10.1), 8.53, 0.9, color="green")
plt.gca().add_patch(rect)
rect = Rectangle((0,10.1), 8.53, 0.9, color="blue",fill=False, hatch="|", linewidth=0.0)
plt.gca().add_patch(rect)

rect = Rectangle((0,11), 8.53, 1.5, color="orange")
plt.gca().add_patch(rect)
rect = Rectangle((0,11), 8.53, 1.5, color="blue",fill=False, hatch="|||", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,12.5), 4.265, 0.1, color="orange")
plt.gca().add_patch(rect)
rect = Rectangle((4.265,12.5), 4.265, 0.1, color="orange")
plt.gca().add_patch(rect)
rect = Rectangle((4.265,12.5), 4.265, 0.1, color="blue",fill=False, hatch="xxx", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,12.6), 8.53, 0.7, color="red")
plt.gca().add_patch(rect)
rect = Rectangle((0,12.6), 8.53, 0.7, color="blue",fill=False, hatch="xxx", linewidth=0.0)
plt.gca().add_patch(rect)

rect = Rectangle((0,13.3), 8.53, 0.1, color="orange")
plt.gca().add_patch(rect)
rect = Rectangle((0,13.3), 8.53, 0.1, color="blue",fill=False, hatch="|", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((0,13.4), 8.53, 0.1, color="red")
plt.gca().add_patch(rect)
rect = Rectangle((0,13.5), 4.265, 0.1, color="red")
plt.gca().add_patch(rect)
rect = Rectangle((0,13.5), 4.265, 0.1, color="blue",fill=False, hatch="|||", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((4.265,13.5), 4.265, 0.1, color="red")
plt.gca().add_patch(rect)
rect = Rectangle((4.265,13.5), 4.265, 0.1, color="blue",fill=False, hatch="|", linewidth=0.0)
plt.gca().add_patch(rect)

rect = Rectangle((0,13.6), 4.265, 0.2, color="orange")
plt.gca().add_patch(rect)
rect = Rectangle((0,13.6), 4.265, 0.2, color="blue",fill=False, hatch="///", linewidth=0.0)
plt.gca().add_patch(rect)
rect = Rectangle((4.265,13.6), 4.265, 0.2, color="red")
plt.gca().add_patch(rect)
rect = Rectangle((4.265,13.6), 4.265, 0.2, color="blue",fill=False, hatch="///", linewidth=0.0)
plt.gca().add_patch(rect)



# x=range(0)
# ax.bar([0,1],[8.53,8.53],facecolor="teal",hatch="///",bottom=base)
# base = [8.53,8.53]
# ax.bar([0,1],[8.91,8.91],facecolor="teal",hatch="|||", bottom=base)
# base=[8.91,8.91]
# ax.bar([0,1],[8.93,8.93],facecolor="teal",hatch="xxx", bottom=base)
# base=[8.93,8.93]
# ax.bar(np.array([0,1]),np.array([12.21,12.21]),facecolor="teal",hatch="|", bottom=np.array(base))
# cir = Circle((0,0), 0.921, lw=4, color=(0,0.4,0,0.4))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.921, lw=4, color=(0,0.4,0,0.4))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.921, lw=4, color=(0,0.4,0,0.4))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.921, lw=4, color=(0,0.4,0,0.4))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.921, lw=4, color=(0,0.4,0,0.4))
# plt.gca().add_patch(cir)

# cir = Circle((0,0), 0.921, lw=2.3, color=(0,0.4,0,1))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.898, lw=0.5,color=(0,0.8,0,1))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.893, lw=0.2, color=(0,0.6,0,1))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.891, lw=3.8, color=(0,0.2,0,1))
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.853, lw=1, color=(0,1,0,1))
# plt.gca().add_patch(cir)


# cir = Circle((0,0), 0.5, lw=1, color="teal")
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.5, lw=1, color="teal")
# plt.gca().add_patch(cir)
# cir = Circle((0,0), 0.5, lw=1, color="teal")
# plt.gca().add_patch(cir)

# plt.gca().add_patch(rect)
# circle1 = plt.Circle((0, 0), 0.2, hatch="///", color='r', )
# circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
# circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)

# fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

# ax.add_patch(circle1)
# ax.add_patch(circle2)
# ax.add_patch(circle3)
plt.tight_layout()

plt.savefig('plots/plotcircles.png')