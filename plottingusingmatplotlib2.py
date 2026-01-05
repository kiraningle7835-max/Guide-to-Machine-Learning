# importing modules
import numpy as np
import matplotlib.pyplot as plt

# X-axis values
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Y-axis values
y1 = [0, 3, 6, 9, 12, 15, 18, 21, 24]
# Y-axis values
y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Function to plot
plt.plot(y1, label="y = 3x")
plt.plot(y2, label="y = x")

# Function add a legend
plt.legend(loc="upper right",ncol=1)
plt.show()