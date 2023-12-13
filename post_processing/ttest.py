from scipy.stats import ttest_ind, ttest_1samp
import numpy as np
sample1 = np.array([14,11,6,5,12,9,13,10,8,13])
sample2 = np.array([5,10,8,6,9,3,10,9,9,9,6,10,5,7,8,5,9,7,9,4])
print(np.mean(sample2))
print(np.mean(sample1))

t_stat, p_value = ttest_ind(sample1, sample2)
print("T-statistic value: ", t_stat)  
print("P-Value: ", p_value)

t_stat, p_value = ttest_1samp(sample2, popmean=7.4)
print("T-statistic value: ", t_stat)  
print("P-Value: ", p_value)