import numpy as np
import matplotlib.pyplot as plt

# Set up the grid
xmin, xmax, ymin, ymax = -2, 2, -2, 2
npts = 500
x, y = np.meshgrid(np.linspace(xmin, xmax, npts), np.linspace(ymin, ymax, npts))
c = complex(-0.8, 0.156)
z = x + 1j*y

# Iterate the Julia set equation
for i in range(100):
    z = z**2 + c

# Create the plot
plt.imshow(np.abs(z), extent=(xmin, xmax, ymin, ymax), cmap='hot')
plt.axis('off')
plt.show()
