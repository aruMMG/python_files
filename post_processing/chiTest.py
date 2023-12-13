import scipy.stats as st
import numpy as np

def chi_p_value(arr):
    exp = st.chi2_contingency(arr)
    val = ((arr-exp[3])**2/exp[3]).sum()
    p = 1-st.chi2.cdf(x=val, df=1)
    return val, p

arr = np.zeros((2,2), dtype=float)
arr[0,0] = 5
arr[1,0] = 14
arr[0,1] = 139
arr[1,1] = 130

val, p = chi_p_value(arr)
print(val)
print(p)