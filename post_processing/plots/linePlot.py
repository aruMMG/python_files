from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

mAP50_10, mAP50_20, mAP50_40, mAP50_80, mAP_10, mAP_20, mAP_40, mAP_80 = [], [], [], [], [], [], [], []

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



X = [1,2,3,4,5,6,7,8,9,10]
Y = [1,2,3,4,5,6,7,8,9,10]

fig = plt.figure(figsize=(3.6,3.6), dpi=600)
ax = fig.add_subplot(111)

ax.plot([1,2,3,4, 5], mAP_10, marker="v")
ax.plot([1,2,3,4, 5], mAP_20, marker="o")
ax.plot([1,2,3,4, 5], mAP_40, marker="s")
ax.plot([1,2,3,4, 5], mAP_80, marker="p")
### axix labels
plt.xlabel('Synth-Added', fontsize=10, fontweight='bold', color="r")
plt.ylabel('mAP', fontsize=10, fontweight='bold')
# ax.xaxis.label.set_color('red')
# ax.yaxis.label.set_color('red')

### axis tick parameters
# ax.set_xticks(range(-1,13,2))
ax.set_yticks(np.arange(0.3,0.8,0.1))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='minor', labelsize=8)
x_labels = [0, 0, 10, 20, 40, 80]
### Change "ax.get_xticks()" to x_labels for manual x_tick label set
### add "weight='bold'" if required
ax.set_xticklabels(x_labels, rotation=0, size=10) 
# ax.set_yticklabels(ax.get_yticks(), rotation=0, weight='bold', size=10)


# axis line setup
# ax.spines['bottom'].set_color('red')
# ax.spines['top'].set_color('red')
# ax.tick_params(axis='x', colors='red') #    axis only tick parameter

plt.tight_layout()
fig.savefig("plots/mAP_line_plot.png")

