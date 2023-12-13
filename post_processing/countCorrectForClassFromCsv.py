import pandas as pd
import csv

path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/split_class.csv"
save_path = "/home/sakuni/phd/dataset_paper/final_collection25-2/lc3/results/classWiseTrue.csv"
csv_df = pd.read_csv(path)

class_name = ["cal", "small", "small_bs", "big", "big_bs", "con", "con_bs", "con_dif", "con_dif_bs"]
total = ["total",  0,0,0,0,0,0,0,0]
true30 = ["true30",  0,0,0,0,0,0,0,0]
trueHdr = ["trueHdr",  0,0,0,0,0,0,0,0]
trueHsv = ["trueHsv",  0,0,0,0,0,0,0,0]

for i, row in csv_df.iterrows():
    if row["class_name"]=="big":
        total[3]+=1
        if row["isPred30"]==1:
            true30[3]+=1
        if row["isPredHdr"]==1:
            trueHdr[3]+=1
        if row["isPredHsv"]==1:
            trueHsv[3]+=1
    if row["class_name"]=="small":
        total[1]+=1
        if row["isPred30"]==1:
            true30[1]+=1
        if row["isPredHdr"]==1:
            trueHdr[1]+=1
        if row["isPredHsv"]==1:
            trueHsv[1]+=1
    if row["class_name"]=="big_bs":
        total[4]+=1
        if row["isPred30"]==1:
            true30[4]+=1
        if row["isPredHdr"]==1:
            trueHdr[4]+=1
        if row["isPredHsv"]==1:
            trueHsv[4]+=1
    if row["class_name"]=="small_bs":
        total[2]+=1
        if row["isPred30"]==1:
            true30[2]+=1
        if row["isPredHdr"]==1:
            trueHdr[2]+=1
        if row["isPredHsv"]==1:
            trueHsv[2]+=1
    if row["class_name"]=="contrast":
        total[5]+=1
        if row["isPred30"]==1:
            true30[5]+=1
        if row["isPredHdr"]==1:
            trueHdr[5]+=1
        if row["isPredHsv"]==1:
            trueHsv[5]+=1
    if row["class_name"]=="contrast_bs":
        total[6]+=1
        if row["isPred30"]==1:
            true30[6]+=1
        if row["isPredHdr"]==1:
            trueHdr[6]+=1
        if row["isPredHsv"]==1:
            trueHsv[6]+=1
    if row["class_name"]=="contrast_dif":
        total[7]+=1
        if row["isPred30"]==1:
            true30[7]+=1
        if row["isPredHdr"]==1:
            trueHdr[7]+=1
        if row["isPredHsv"]==1:
            trueHsv[7]+=1
    if row["class_name"]=="contrast_dif":
        total[8]+=1
        if row["isPred30"]==1:
            true30[8]+=1
        if row["isPredHdr"]==1:
            trueHdr[8]+=1
        if row["isPredHsv"]==1:
            trueHsv[8]+=1
csv_file = []
csv_file.append(class_name)
csv_file.append(total)
csv_file.append(true30)
csv_file.append(trueHdr)
csv_file.append(trueHsv)

with open(save_path, "w") as f:
    write = csv.writer(f)
    write.writerows(csv_file)