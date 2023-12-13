import matplotlib.pyplot as plt
import pandas as pd

path = "/home/sakuni/phd/Experiments/hdr/python/lc3/lc4/lc4_small_variance.csv"

df = pd.read_csv(path)

groups = df.groupby("class_name")
fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
for name, group in groups:
    # print("name:{}".format(name))
    # print("avg:{}, serial No:{}".format(group.avg,group.index.values))
    if name.startswith("big"):
        color = (1,0,0,1)
        ax.plot(group.avg, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
    else:
        color = (0,1,0,1)
        ax.plot(group.avg, group.variance, color=color, marker='o', linestyle='',markersize=2,label=name)
ax.set_xlabel('Average')
ax.set_ylabel('Variance')
plt.savefig("lc4_avg_variance.png",bbox_inches='tight')