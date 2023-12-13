with open("/home/sakuni/phd/results/p2/test/all/mAP.csv", "r") as f:
    lines = f.readlines()
    mAP50_10, mAP50_20, mAP50_40, mAP50_80, mAP_10, mAP_20, mAP_40, mAP_80 = [], [], [], [], [], [], [], []
    for i, line in enumerate(lines):
        line_lis = line.split(",")
        if i<2:
            continue
        elif i<7:
            mAP_10.append(float(line_lis[-1]))
            mAP50_10.append(float(line_lis[-3]))
        elif i<12:           
            mAP_20.append(float(line_lis[-1]))
            mAP50_20.append(float(line_lis[-3]))
        elif i<17:           
            mAP_40.append(float(line_lis[-1]))
            mAP50_40.append(float(line_lis[-3]))
        elif i<22:           
            mAP_80.append(float(line_lis[-1]))
            mAP50_80.append(float(line_lis[-3]))
print(mAP_10)
print(mAP_20)
print(mAP_40)
print(mAP_80)
