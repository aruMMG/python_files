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
    if name == "big":
        color = (1,0,0,1)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)

    elif name == "big_bs":
        color = (1,0,0,0.5)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    elif name == "big_bs_nc":
        color = (1,0,0,0.25)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    elif name == "small":
        color = (0,1,0,1)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    elif name == "small_bs":
        color = (0,1,0,0.5)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    elif name == "contrast":
        color = (0,0,1,1)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    elif name == "contrast_bs":
        color = (0,0,1,0.5)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    elif name == "contrast_dif":
        color = (0.5,0.5,0.5,0)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    elif name == "contrast_dif_bs":
        color = (0.5,0.5,0.5,0.5)
        ax.plot(group.index.values, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    else:
        print("class not found:{}".format(name))
        
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
plt.savefig("variance.png",bbox_inches='tight')
