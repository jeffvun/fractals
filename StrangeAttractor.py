import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz attractor function
def lorenz(x, y, z, s=10, r=28, b=8/3):
    dx = s * (y - x)
    dy = r * x - y - x * z
    dz = x * y - b * z
    return dx, dy, dz

# Runge-Kutta 4th order method for solving ODEs
def rk4(f, x0, y0, z0, h=0.01, n=10000):
    xs = np.zeros(n)
    ys = np.zeros(n)
    zs = np.zeros(n)
    xs[0], ys[0], zs[0] = x0, y0, z0
    for i in range(1, n):
        k1x, k1y, k1z = f(xs[i-1], ys[i-1], zs[i-1])
        k2x, k2y, k2z = f(xs[i-1] + 0.5*h*k1x, ys[i-1] + 0.5*h*k1y, zs[i-1] + 0.5*h*k1z)
        k3x, k3y, k3z = f(xs[i-1] + 0.5*h*k2x, ys[i-1] + 0.5*h*k2y, zs[i-1] + 0.5*h*k2z)
        k4x, k4y, k4z = f(xs[i-1] + h*k3x, ys[i-1] + h*k3y, zs[i-1] + h*k3z)
        xs[i] = xs[i-1] + (h/6)*(k1x + 2*k2x + 2*k3x + k4x)
        ys[i] = ys[i-1] + (h/6)*(k1y + 2*k2y + 2*k3y + k4y)
        zs[i] = zs[i-1] + (h/6)*(k1z + 2*k2z + 2*k3z + k4z)
    return xs, ys, zs

# Set initial conditions
x0, y0, z0 = 1, 1, 1

# Compute trajectory using Runge-Kutta 4th order method
xs, ys, zs = rk4(lorenz, x0, y0, z0)

# Plot 3D trajectory
fig = plt.figure()
# ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
