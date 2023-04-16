import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mandelbulb(x, y, z, power, degree, max_iterations):
    c = complex(x, y)
    for i in range(max_iterations):
        r = abs(c)
        theta = np.arctan2(np.sqrt(x**2 + y**2), z)
        phi = degree * np.arctan2(y, x)
        c = (r**power) * complex(np.sin(theta*power)*np.cos(phi*power), np.sin(theta*power)*np.sin(phi*power))
        c += complex(z, 0)
        if abs(c) > 2:
            return i
    return max_iterations

power = 8
degree = 3
max_iterations = 50
num_points = 100

x = np.linspace(-1, 1, num_points)
y = np.linspace(-1, 1, num_points)
z = np.linspace(-1, 1, num_points)

fractal = np.zeros((num_points, num_points, num_points))

for i in range(num_points):
    for j in range(num_points):
        for k in range(num_points):
            fractal[i,j,k] = mandelbulb(x[i], y[j], z[k], power, degree, max_iterations)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.voxels(fractal, edgecolor='k')

fig.set_size_inches(8, 8)
plt.savefig('mandelbulb.png', dpi=300)
plt.show()
