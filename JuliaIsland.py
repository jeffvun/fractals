import numpy as np
import matplotlib.pyplot as plt


# Function to calculate the Julia Set
def julia(c, z, max_iterations):
    for n in range(max_iterations):
        if abs(z) > 2:
            return n
        z = z ** 2 + c
    return max_iterations


# Define the constants for the Julia Set
c = complex(-0.835, -0.2321)
xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
resolution = 1000
max_iterations = 1000

# Create a grid of complex numbers
X = np.linspace(xmin, xmax, resolution)
Y = np.linspace(ymin, ymax, resolution)
Z = np.array([complex(x, y) for y in Y for x in X])
Z = Z.reshape((resolution, resolution))

# Calculate the Julia Set for each point in the grid
julia_set = np.array([[julia(c, z, max_iterations) for z in row] for row in Z])

# Plot the Julia Island
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.imshow(julia_set.T, cmap='inferno', extent=[xmin, xmax, ymin, ymax])
ax.axis('off')
plt.show()
