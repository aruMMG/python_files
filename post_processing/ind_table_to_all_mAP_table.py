import csv
import os
import pandas as pd
from pathlib import Path
def combine_results(res_paths, final_table=[]):
    final_table = [["exp", 0.5, 0.75, "mAP", 0.5, 0.75, "mAP", 0.5, 0.75, "mAP", 0.5, 0.75, "mAP", 0.5, 0.75, "mAP", 0.5, 0.75, "mAP"]]
    for res_path in res_paths:
        path_name = res_path.split("/")[-2]
        print(path_name)
        df = df = pd.read_csv(res_path, header=None, skiprows=1)
        columns = pd.read_csv(res_path, nrows=0).columns.tolist()
        num_missing_cols = len(df.columns) - len(columns)
        new_cols = ['col' + str(i+1) for i in range(num_missing_cols)]
        df.columns = columns + new_cols
        lis_tab = [path_name]
        for idx,rows in df.iterrows():
            lis_tab.append(rows["0.5"])
            lis_tab.append(rows["0.75"])
            lis_tab.append(rows["mAP"])
        avg = df[["0.5", "0.75", "mAP"]].mean()
        lis_tab.append(avg[0])
        lis_tab.append(avg[1])
        lis_tab.append(avg[2])
        final_table.append(lis_tab)
    return final_table
if __name__=="__main__":
    results_paths = [
                    "/home/sakuni/phd/results/p2/test/all/10_real/10_real/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/10_real/10_real_10_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/10_real/10_real_20_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/10_real/10_real_40_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/10_real/10_real_80_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/20_real/20_real/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/20_real/20_real_10_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/20_real/20_real_20_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/20_real/20_real_40_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/20_real/20_real_80_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/40_real/40_real/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/40_real/40_real_10_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/40_real/40_real_20_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/40_real/40_real_40_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/40_real/40_real_80_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/80_real/80_real/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/80_real/80_real_10_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/80_real/80_real_20_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/80_real/80_real_40_synth/resultsAP.csv",
                    "/home/sakuni/phd/results/p2/test/all/80_real/80_real_80_synth/resultsAP.csv",

                    ]
    save_path = "/home/sakuni/phd/results/p2/test/all/mAP.csv"
    csv_table = combine_results(res_paths=results_paths)
    with open(save_path, "w") as f:
        wr = csv.writer(f)
        wr.writerows(csv_table)