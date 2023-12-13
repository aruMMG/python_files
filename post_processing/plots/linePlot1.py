from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

mAP50_R = [0.857,
            0.940,
            0.969,
            0.978,
            ]
mAP50_imp = [0.921,0.953,0.981,0.981]




X = [1,2,3,4,5,6,7,8,9,10]
Y = [1,2,3,4,5,6,7,8,9,10]

fig = plt.figure(figsize=(3.6,3.6), dpi=600)
ax = fig.add_subplot(111)

ax.plot([1,2,3,4], mAP50_R, marker="v")
ax.plot([1,2,3,4], mAP50_imp, marker="o")

### axix labels
plt.xlabel('Real-Images', fontsize=10, fontweight='bold')
plt.ylabel('mAP', fontsize=10, fontweight='bold')
# ax.xaxis.label.set_color('red')
# ax.yaxis.label.set_color('red')

### axis tick parameters
# ax.set_xticks(range(-1,13,2))
ax.set_yticks(np.arange(0.8,1.01,0.05))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='minor', labelsize=8)
x_labels = [0, 10, 20, 40, 80]
### Change "ax.get_xticks()" to x_labels for manual x_tick label set
### add "weight='bold'" if required
ax.set_xticklabels(x_labels, rotation=0, size=10) 
# ax.set_yticklabels(ax.get_yticks(), rotation=0, weight='bold', size=10)

plt.legend(["Real", "+ Synth"], loc ="lower right")
# axis line setup
# ax.spines['bottom'].set_color('red')
# ax.spines['top'].set_color('red')
# ax.tick_params(axis='x', colors='red') #    axis only tick parameter

plt.tight_layout()
fig.savefig("plots/mAP_line_plot_synth_imp.png")

