import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the maximum number of iterations
MAX_ITERS = 20

# Define the size of the grid
GRID_SIZE = 100

# Define the size of the box
BOX_SIZE = 2

# Define the value of the exponent
POWER = 8

# Define the function to calculate the Mandelbulb
def mandelbulb(z, power):
    r = np.abs(z)
    theta = np.arctan2(z.imag, z.real)
    phi = np.arctan2(np.sqrt(z.real**2 + z.imag**2), z.imag)
    new_r = r ** power
    new_theta = power * theta
    new_phi = power * phi
    real_part = new_r * np.sin(new_phi) * np.cos(new_theta)
    imag_part = new_r * np.sin(new_phi) * np.sin(new_theta)
    return real_part + 1j * imag_part + z

# Define the function to calculate the Mandelbulb set
def mandelbulb_set(xmin, xmax, ymin, ymax, zmin, zmax, grid_size, power, max_iters):
    x, y, z = np.ogrid[xmin:xmax:grid_size*1j, ymin:ymax:grid_size*1j, zmin:zmax:grid_size*1j]
    c = x + y*1j + z*1j
    mask = np.ones(c.shape, dtype=bool)
    z = c
    for i in range(max_iters):
        z = mandelbulb(z, power)
        mask &= (np.abs(z) < 2)
    return mask

# Generate the Mandelbulb set
mask = mandelbulb_set(-BOX_SIZE, BOX_SIZE, -BOX_SIZE, BOX_SIZE, -BOX_SIZE, BOX_SIZE, GRID_SIZE, POWER, MAX_ITERS)

# Plot the Mandelbulb set
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = np.indices(mask.shape)
ax.voxels(x, y, z, mask)
plt.show()
