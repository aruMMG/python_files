"""
required save path to save the confusionMatrix plot. And a array and detection class names
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def plot(matrix, save_dir='', names=(), nc=1, safe=False):

    import seaborn as sn

    array = matrix # / (self.matrix.sum(0).reshape(1, self.nc + 1) + 1E-6)  # normalize
    #array[array < 0.005] = np.nan  # don't annotate (would appear as 0.00)

    fig = plt.figure(figsize=(12, 9))
    sn.set(font_scale=1.0 if nc < 50 else 0.8)  # for label size
    labels = (0 < len(names) < 99) and len(names) == nc  # apply names to ticklabels

    sn.heatmap(array, annot=nc < 30, annot_kws={"size": 8}, cmap='Purples', fmt='.2f', square=True,
                xticklabels=names + ['background'] if labels else "auto",
                yticklabels=names + ['background'] if labels else "auto").set_facecolor((1, 1, 1))
    fig.axes[0].set_xlabel('True')
    fig.axes[0].set_ylabel('Predicted')
    fig.tight_layout()
    if safe:
        fig.savefig(Path(save_dir) / 'confusionMatrixSafeInclude.png', dpi=300)
    else:
        fig.savefig(Path(save_dir) / 'confusionMatrix.png', dpi=250)


if __name__=="__main__":
    name = ["splits"]
    save_dir = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc4/results/3_images/test"
    index00 = 140
    index01 = 7
    index10 = 4
    index01s = 19
    matrix = np.array([[index00, index01], [index10,0]])
    plot(matrix, save_dir=save_dir,names=name)
    matrix = np.array([[index00, index01s], [index10,0]])
    plot(matrix, save_dir=save_dir,names=name, safe=True)