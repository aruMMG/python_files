import os
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import seaborn as sns

path = "/home/sakuni/phd/Experiments/hdr/python/lc3"

data = pd.read_csv(os.path.join(path,"variance_only.csv"))

groups = data.groupby("class_name")
fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
for name, group in groups:
    # print("name:{}".format(name))
    # print("avg:{}, serial No:{}".format(group.avg,group.index.values))
    if name in ["big","big_bs","small","contrast","big_bs_nc"]:
        color = (0,1,0,1)
        name = "easy"
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)

    elif name in ["small_bs","contrast_bs","contrast_dif","contrast_dif_bs"]:
        color = (0,0,1,1)
        name = "hard"
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)

    else:
        print("class not found")
        
# sns_plot = sns.scatterplot("avg", x, data=data, hue="class_name")
# fig = sns_plot.get_figure()
# fig.savefig("avg_only.png")
# print(len(y))
# colors = {"contrast":"red","contrast_dif":"green","contrast_bs":"blue","contrast_dif_bs":"cyan","small":"magenta","small_bs":"yellow","big":"black","big_bs":"white","big_bs_nc":"white"}
# fig = plt.figure()
# ax=fig.add_axes([0,0,1,1])
# ax.scatter(x, y, c=data['class_name'].map(colors))
ax.set_xlabel('image number')
ax.set_ylabel('Difference')
plt.savefig("variance_easy_hard_type2.png",bbox_inches='tight')
