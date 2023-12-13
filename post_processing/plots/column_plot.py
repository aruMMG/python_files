from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

mAP50_0, mAP50_10, mAP50_20, mAP50_40, mAP50_80,mAP_0, mAP_10, mAP_20, mAP_40, mAP_80 = [],[], [], [], [], [], [], [], [], []

with open("/home/sakuni/phd/results/p2/test/all/mAP.csv", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line_lis = line.split(",")
        if i<2:
            continue
        elif (i-2)%5==1:
            mAP_10.append(float(line_lis[-1]))
            mAP50_10.append(float(line_lis[-3]))
        elif (i-2)%5==2:           
            mAP_20.append(float(line_lis[-1]))
            mAP50_20.append(float(line_lis[-3]))
        elif (i-2)%5==3:           
            mAP_40.append(float(line_lis[-1]))
            mAP50_40.append(float(line_lis[-3]))
        elif (i-2)%5==4:           
            mAP_80.append(float(line_lis[-1]))
            mAP50_80.append(float(line_lis[-3]))
        elif (i-2)%5==0:           
            mAP_0.append(float(line_lis[-1]))
            mAP50_0.append(float(line_lis[-3]))


print(mAP_0)
print(mAP_10)
print(mAP_20)
print(mAP_40)
print(mAP_80)
X = np.arange(4)


base_val = 0.8

mAP50_0 = [i-base_val for i in mAP50_0]
mAP50_10 = [i-base_val for i in mAP50_10]
mAP50_20 = [i-base_val for i in mAP50_20]
mAP50_40 = [i-base_val for i in mAP50_40]
mAP50_80 = [i-base_val for i in mAP50_80]
base = np.ones(len(mAP50_10))*base_val
print(X)
fig = plt.figure(figsize=(7.1,3.6), dpi=600)
ax = fig.add_subplot(111)

ax.bar(X-0.3, mAP50_0, bottom=base, width=0.15,color=[(0.2,0.2,0.2)])
ax.bar(X-0.15, mAP50_10, bottom=base, width=0.15,color=[(0.35,0.35,0.35)])
ax.bar(X, mAP50_20, bottom=base, width=0.15,color=[(0.5,0.5,0.5)])
ax.bar(X+0.15, mAP50_40, bottom=base, width=0.15,color=[(0.65,0.65,0.65)])
ax.bar(X+0.3, mAP50_80, bottom=base, width=0.15,color=[(0.8,0.8,0.8)])
# ax.plot([1,2,3,4, 5], mAP_20, marker="o"
### axix labels
plt.xlabel('Real_Images', fontsize=10, fontweight='bold')
plt.ylabel('mAP50', fontsize=10, fontweight='bold')
# ax.xaxis.label.set_color('red')
# ax.yaxis.label.set_color('red')

### axis tick parameters
# ax.set_xticks(range(-1,13,2))
ax.set_yticks(np.arange(base_val,1.01,0.05))
ax.set_xticks(np.arange(4))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='minor', labelsize=8)
x_labels = [10, 20, 40, 80]
### Change "ax.get_xticks()" to x_labels for manual x_tick label set
### add "weight='bold'" if required
ax.set_xticklabels(x_labels, rotation=0, size=10) 
# ax.set_yticklabels(ax.get_yticks(), rotation=0, weight='bold', size=10)


# axis line setup
# ax.spines['bottom'].set_color('red')
# ax.spines['top'].set_color('red')
# ax.tick_params(axis='x', colors='red') #    axis only tick parameter

plt.tight_layout()
fig.savefig("plots/c.png")