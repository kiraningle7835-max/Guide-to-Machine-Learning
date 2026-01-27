import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Reading the CSV file
# Make sure the CSV has two columns: one feature (X) and one target (y)
data = pd.read_csv("/mnt/data/data (2).csv")
# Assuming first column is input feature and second column is output
X = data.iloc[:, 0].values
y = data.iloc[:, 1].values
# Reshaping X because gradient descent math works better this way
X = X.reshape(-1, 1)
X_mean = np.mean(X)
X_std = np.std(X)
X = (X - X_mean) / X_std
m = 0
c = 0
learning_rate = 0.01
epochs = 1000
n = len(X)
for i in range(epochs):
    
    # Predicted values using current m and c
    y_pred = m * X.flatten() + c
    
    # Calculate gradients
    dm = (-2/n) * np.sum((y - y_pred) * X.flatten())
    dc = (-2/n) * np.sum(y - y_pred)
    
    # Update parameters
    m = m - learning_rate * dm
    c = c - learning_rate * dc
    if i % 100 == 0:
        loss = np.mean((y - y_pred) ** 2)
        print(f"Epoch {i}, Loss: {loss:.4f}")
y_final = m * X.flatten() + c
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_final, color='red', label='Regression Line')
plt.xlabel("Input Feature")
plt.ylabel("Target Value")
plt.title("Linear Regression from Scratch")
plt.legend()
plt.show()
print("Final slope (m):", m)
print("Final intercept (c):", c)
