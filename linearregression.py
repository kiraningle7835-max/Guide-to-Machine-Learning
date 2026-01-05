import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
df = pd.read_csv('data.csv')
df = df[['Duration', 'Pulse']]
df.dropna(inplace=True)
x=np.array([1,2,3,4,5,6,7,8,9]).reshape(-1,1)
y=x*2
x1, x2, y1, y2=train_test_split(x,y,test_size=0.25)
regr=LinearRegression()
regr.fit(x1,y1)
pr=regr.predict(x2)
plt.scatter(x2,y2,c="Green")
plt.plot(x2,pr,"o:b")
plt.show()
print(regr.score(x2,y2))


