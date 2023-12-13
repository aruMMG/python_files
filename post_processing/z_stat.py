import math
import scipy.stats as st
import stat
import numpy as np
def zValue(arr):
    """
    input: arr(2,2)
    output: z-value and p-value

    arr(2, 2): rows are two method comparing for the null hypothesis,
                columns are number of time sucessed or not sucessed
                last column and last row are total
    """

    probA = arr[0,0]/arr[0,1]
    probB = arr[1,0]/arr[1,1]
    p_cap = (arr[0,0]+arr[1,0])/(arr[0,1]+arr[1,1])
    zvalue = (probA-probB)/math.sqrt(p_cap*(1-p_cap)*(1/arr[0,1]+1/arr[1,1]))
    
    p = (1-st.norm.cdf(abs(zvalue)))*2
    return zvalue, p
