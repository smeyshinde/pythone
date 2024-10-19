# -------------------------------------------I use the resolved fromula in this code and for derivation for this is also avaliable----------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# User input for generating random data
n_samples = int(input("Enter the number of samples: "))
x_min = float(input("Enter the minimum value for X: "))
x_max = float(input("Enter the maximum value for X: "))
noise_level = float(input("Enter the noise level: "))
alpha = float(input("Enter the regularization parameter (alpha): "))

# Seed for reproducibility
np.random.seed(42)

# Generating random data based on user input
X = np.random.rand(n_samples, 1) * (x_max - x_min) + x_min
y = 2 + 0.5 * X**2 - 3 * X + np.random.randn(n_samples, 1) * noise_level

# Display the randomly generated data
print("Randomly Generated Data (X, y):")
for i in range(n_samples):
    print(f"X: {X[i][0]:.2f}, y: {y[i][0]:.2f}")

# Adding polynomial features (degree 2) manually
X_poly = np.hstack((X, X**2))

# Adding bias term (ones column) for intercept
X_poly_bias = np.hstack([np.ones((n_samples, 1)), X_poly])

# Ridge regression closed-form solution: theta = (X.T * X + alpha * I)^-1 * X.T * y
I = np.eye(X_poly_bias.shape[1])
I[0, 0] = 0  # Do not regularize the bias term
theta_ridge = np.linalg.inv(X_poly_bias.T @ X_poly_bias + alpha * I) @ X_poly_bias.T @ y

# Predicting values using Ridge Regression model
y_pred_ridge = X_poly_bias @ theta_ridge

# Plotting the results
plt.scatter(X, y, color='cyan', label='Original Data')
plt.scatter(X, y_pred_ridge, color='green', label='Ridge Regression')
plt.title('Ridge Regression (Manual)')
plt.legend()
plt.show()

# Display theta values
print(f"Ridge Regression Coefficients (theta): {theta_ridge.ravel()}")
