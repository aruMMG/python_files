import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data
path_xl = "/home/sakuni/phd/Experiments/hdr/calibration/test6/test_data.csv"

data = pd.read_csv(path_xl, header=[0,1])

# Organize data
cols = pd.MultiIndex.from_tuples([("image_name",), ("cs150_reading", "X"), ("cs150_reading", "Y"), ("cs150_reading", "Z"),
                ("ls150_reading",), ("Location", "Region"), ("Location", "x1"), ("Location", "y1"), ("Calculated", "X"), ("Calculated", "Y"), 
                ("Calculated", "Z"),("avg_Y",),("Ratio", "X"), ("Ratio", "Y"), ("Ratio", "Z")])
data.columns = cols


"""
## Learning
X_plot = data.Calculated.Y
X= np.array([[np.log(i),1] for i in data.Calculated['Y']])
y=data.avg_Y
beta = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(y))

## Prediction
predx = np.linspace(min(data.Calculated['Y']),max(data.Calculated['Y']),200)
X_pred = np.array([[np.log(i),1] for i in predx])
predy = X_pred.dot(beta)

"""
X = data.Calculated[["Y"]]
x_for_plot=data.Calculated.Y
Y = data.avg_Y


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


pre_process = PolynomialFeatures(degree=2)
X_poly = pre_process.fit_transform(X)


pr_model = LinearRegression()
pr_model.fit(X_poly,Y)

predx = np.linspace(min(x_for_plot),max(x_for_plot),200).reshape(-1,1)
predx_poly = pre_process.fit_transform(predx)


predy = pr_model.predict(predx_poly)

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(X, Y, color='r')
ax.set_xlabel('Calculated Y')
ax.set_ylabel('Measured Y')
ax.set_title('Polynomial fitting')
ax.plot(predx,predy, lw = 3, color = 'g')
plt.savefig("test6_avg_Y.png",bbox_inches='tight')

from sklearn.metrics import r2_score
Y_pred = pr_model.predict(X_poly)
print(r2_score(Y,Y_pred))
print(pr_model.coef_, pr_model.intercept_)

x = np.array([[0,1,10,30,100,300, 600, 1000,1700]]).T
pre_process = PolynomialFeatures(degree=2)
X = pre_process.fit_transform(x)
print(X)
print(pr_model.predict(X))
"""
import cv2
path = "/home/sakuni/phd/Experiments/hdr/calibration/test1/exr/hdr9.exr"
image = cv2.imread(path, flags=cv2.IMREAD_ANYDEPTH+cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)

y=pre_process.fit_transform(image[:,:,1])
print(image[3000,1600,1])
lum = pr_model.predict(y)
print(y.shape)
print(image[:,:,1].shape)
print(lum.shape)
"""