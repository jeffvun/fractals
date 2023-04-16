import numpy as np
import matplotlib.pyplot as plt

# Define the constants
x_min, x_max = -2.5, 1.5
y_min, y_max = -2, 2
max_iterations = 100
resolution = 500

# Create the complex plane
x = np.linspace(x_min, x_max, resolution)
y = np.linspace(y_min, y_max, resolution)
c = x[:, np.newaxis] + 1j*y[np.newaxis, :]

# Create the fractal
fractal = np.zeros((resolution, resolution), dtype=np.float32)
for i in range(max_iterations):
    fractal += np.abs(c) < 2
    z = np.abs(c)**2 + c
    c = z

# Convert fractal to float type for display
fractal = fractal.astype(np.float32)

# Display the fractal
plt.imshow(fractal, cmap='hot', extent=[x_min, x_max, y_min, y_max])
plt.axis('off')
plt.show()
