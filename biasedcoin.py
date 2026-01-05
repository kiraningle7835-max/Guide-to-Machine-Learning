import numpy as np
from numpy import random 
exp=np.random.choice([0,1],size=100000000,p=[0.3,0.7])
ph=np.mean(exp==1)
pt=np.mean(exp==0)
print(ph,pt)