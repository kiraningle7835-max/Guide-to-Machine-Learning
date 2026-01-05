import numpy as np 
from numpy import random as r
n=100000000
d1=r.randint(1,7,size=n)
d2=r.randint(1,7,size=n)
sumtobe11=np.mean(d1+d2==12)
print(sumtobe11)