import pandas as pd

en_df = pd.read_csv("img_entropy_divide.csv")
res_df = pd.read_csv("/home/sakuni/phd/results/best_exp/res_indivisual_04.csv")


count0, count1 = 0,0
true0, true1 = 0,0
for idx, row in res_df.iterrows():
    for en_idx, en_row in en_df.iterrows():
        if row["image_id"]==en_row["image_id"] and row["defect_idx"]==en_row["defect_id"]:
            if int(en_row["en_cl"])==0:
                count0+=1
                if int(row["res"])==1:
                    true0 += 1
            elif int(en_row["en_cl"])==1:
                count1 += 1
                if int(row["res"])==1:
                    true1 += 1
            else:
                print("Error: Entropy divided crack into multiple group")
        else:
            continue

assert count0+count1 == 144, "length of en_cl not matching 144"
print("count of en_cl 0: {}".format(count0))
print("count of en_cl 1: {}".format(count1))
print("true_pred 0: {}".format(true0))
print("true_pred 1: {}".format(true1))