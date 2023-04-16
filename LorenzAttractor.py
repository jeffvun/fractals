import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the Lorenz Attractor
sigma = 10
rho = 28
beta = 8/3

# Define the function to calculate the Lorenz Attractor
def lorenz(x, y, z, sigma, rho, beta):
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return x_dot, y_dot, z_dot

# Define the time step and number of iterations
dt = 0.01
num_iters = 10000

# Initialize the x, y, and z arrays
xs = np.empty(num_iters + 1)
ys = np.empty(num_iters + 1)
zs = np.empty(num_iters + 1)

# Set the initial conditions
xs[0], ys[0], zs[0] = (0, 1, 1.05)

# Calculate the Lorenz Attractor
for i in range(num_iters):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], sigma, rho, beta)
    xs[i+1] = xs[i] + (x_dot * dt)
    ys[i+1] = ys[i] + (y_dot * dt)
    zs[i+1] = zs[i] + (z_dot * dt)

# Plot the Lorenz Attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.show()
