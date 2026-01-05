import numpy as np
from numpy import random 
n=1000000
coin1=random.randint(0,2,size=n)
coin2=random.randint(0,2,size=n)
coin3=random.randint(0,2,size=n)
proballheads=np.mean((coin1==1) & (coin2==1) & (coin3==1))
print(proballheads)
