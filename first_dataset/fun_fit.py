import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data
path_xl = "/home/sakuni/phd/Experiments/hdr/calibration/test6/test_data.csv"

def func(X, A,b,c):
    res = A*(X**b)+c
    #print(res.shape)
    return res

data = pd.read_csv(path_xl, header=[0,1])

# Organize data

cols = pd.MultiIndex.from_tuples([("image_name",), ("cs150_reading", "X"), ("cs150_reading", "Y"), ("cs150_reading", "Z"),
                ("ls150_reading",), ("Location", "Region"), ("Location", "x1"), ("Location", "y1"), ("Calculated", "X"), ("Calculated", "Y"), 
                ("Calculated", "Z"),("avg_Y",),("Ratio", "X"), ("Ratio", "Y"), ("Ratio", "Z")])
data.columns = cols



X = data.iloc[:,9]

Y = data.iloc[:,11]

from scipy.optimize import curve_fit

popt, pcov = curve_fit(func,X,Y)
print(*popt)
predx = np.linspace(min(X),max(X),200).reshape(-1,1)
predy = func(predx,*popt)

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(X, Y, color='r')
ax.set_xlabel('Calculated Y')
ax.set_ylabel('Measured Y')
ax.set_title('Polynomial power function fitting')
ax.plot(predx,predy, lw = 3, color = 'g')
plt.savefig("test6_Y_power_fun2.png",bbox_inches='tight')

from sklearn.metrics import r2_score
Y_pred = func(X, *popt)
print(r2_score(Y,Y_pred))
x = np.array([[0,1,10,30,100,300, 600, 1000,1700]]).T
print(func(x,*popt))
