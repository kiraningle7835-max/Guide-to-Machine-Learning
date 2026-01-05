import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
coloris = np.random.randint(100, size=(100))
sai = 10 * np.random.randint(100, size=(100))
d=np.random.random(size=(100))

plt.scatter(x, y, c=coloris, s=400, alpha=1, cmap='nipy_spectral')

plt.colorbar()

plt.show()