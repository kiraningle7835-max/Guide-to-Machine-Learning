
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

m=random.uniform(low=2,high=3,size=100)
sns.displot(m,kind="kde")
plt.show()










