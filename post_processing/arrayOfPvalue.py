import z_stat
import numpy as np
import pandas as pd
import z_plot
import os
import csv
import chiTest
def statTest(path_1, path_2, col_listFN, iou, conf, test="Z", sample_size=(144,144)):
    path_1_cm = os.path.join(path_1, "CM"+str(iou)+".csv")
    path_2_cm = os.path.join(path_2, "CM"+str(iou)+".csv")



    df_best = pd.read_csv(path_1_cm)
    df_hdr = pd.read_csv(path_2_cm)
    df_best["FN"] = df_best[col_listFN].sum(axis=1)
    df_hdr["FN"] = df_hdr[col_listFN].sum(axis=1)

    arr = np.zeros((2,2), dtype=float)
    
    arr[0,0] = df_best.loc[df_best["conf"] == conf]["FN"]
    arr[1,0] = df_hdr.loc[df_hdr["conf"] == conf]["FN"]
    if test == "Z":
        arr[0,1]=sample_size[0]
        arr[1,1] = sample_size[1]
        z,p = z_stat.zValue(arr)
        return z, p
    elif test=="Chi":
        arr[0,1]=sample_size[0]-arr[0,0]
        arr[1,1]=sample_size[1]-arr[1,0]
        chi2_val, p = chiTest.chi_p_value(arr)
        return chi2_val, p
    
    else:
        print("no test name provided")

path_1 = "/home/sakuni/phd/results/3_images/test/"
path_2 = "/home/sakuni/phd/results/hdr/test/"
confs = [0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75]
ious = [0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
arrofZ = np.zeros((len(ious)+1, len(confs)+1), dtype=float)
arrofZ_safeInclude = np.zeros((len(ious)+1, len(confs)+1), dtype=float)
for c, conf in enumerate(confs):
    for i, iou in enumerate(ious):
            
        arrofZ[0,c+1] = conf
        arrofZ_safeInclude[0,c+1] = conf
        arrofZ[i+1,0] = iou
        arrofZ_safeInclude[i+1,0] = iou
        
        col_listFN = ["FN1", "FN2", "FN3", "FN4", "FN5"]
        col_listFPS = ["FPS1", "FPS2", "FPS3", "FPS4", "FPS5"]

        arrofZ[i+1,c+1] = statTest(path_1, path_2, col_listFN, iou, conf, test="Chi")[1]
        arrofZ_safeInclude[i+1,c+1] = statTest(path_1, path_2, col_listFPS, iou, conf, test="Chi", sample_size=(270,270))[1]

        
        # z_plot.zplot(two_tailed=False, align_right=False, save_dir="/home/aru/phd/hdr/dataset/lc4/results/best_exp/test")

with open("/home/sakuni/phd/results/best_exp/test/chi_3_images_hdr.csv", mode='w') as ap_file:
    ap_writer = csv.writer(ap_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ap_writer.writerows(arrofZ.tolist())
with open("/home/sakuni/phd/results/best_exp/test/chi_3_images_hdr_safe.csv", mode='w') as ap_file:
    ap_writer = csv.writer(ap_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ap_writer.writerows(arrofZ_safeInclude.tolist())

