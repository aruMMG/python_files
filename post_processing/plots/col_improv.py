import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np

mAP50_R = [0.857,
            0.940,
            0.969,
            0.978,
            ]
mAP50_imp = [0.921,0.953,0.981,0.981]
X = np.arange(4)

base_val = 0.8

mAP50_R_plot = [i-base_val for i in mAP50_R]
mAP50_imp_plot = [x-mAP50_R[idx] for idx, x in enumerate(mAP50_imp)]

base = np.ones(len(mAP50_R))*base_val
hatches = ["xx", "xx", "|||", "|||"]
fig = plt.figure(figsize=(3.6,3.6), dpi=600)
ax = fig.add_subplot(111)
# colors = [[(0.3,0.3,0.3)],[(0.3,0.3,0.3)],[(0.8,0.8,0.8)],[(0.8,0.8,0.8)]]
colors = [[(0.8,0.8,0.8)],[(0.8,0.8,0.8)],[(0.8,0.8,0.8)],[(0.8,0.8,0.8)]]
ax.bar(X, mAP50_R_plot, bottom=base, width=0.9,color=[(0,0,0)])
for idx, m in enumerate(mAP50_imp_plot):
    # ax.bar([X[idx]], [m], bottom=[mAP50_R[idx]], width=0.9,color=colors[idx], hatch = hatches[idx])
    ax.bar([X[idx]], [m], bottom=[mAP50_R[idx]], width=0.9,color=colors[idx])

# ax.bar(X, mAP50_imp_plot, bottom=mAP50_R, width=0.9,color=[(0.35,0.35,0.35)],hatch="|")

### axix labels
plt.xlabel('Real-Images', fontsize=10, fontweight='bold')
plt.ylabel('mAP', fontsize=10, fontweight='bold')
# ax.xaxis.label.set_color('red')
# ax.yaxis.label.set_color('red')

### axis tick parameters
# ax.set_xticks(range(-1,13,2))
# ax.set_yticks(np.arange(base_val,1,0.1))
ax.set_xticks(np.arange(4))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='minor', labelsize=8)
x_labels = [10, 20, 40, 80]
### Change "ax.get_xticks()" to x_labels for manual x_tick label set
### add "weight='bold'" if required
ax.set_xticklabels(x_labels, rotation=0, size=10)

# legend
labels = ["Real", "+ Synth"]
colors = [(0,0,0),(0.8,0.8,0.8)]
# colors = ["red", "green"]
handles = [plt.Rectangle((0,0),1,1, color=colors[idx]) for idx in range(len(labels))]
plt.legend(handles, labels)
plt.tight_layout()

plt.savefig('plots/col_imp_mAP.png')