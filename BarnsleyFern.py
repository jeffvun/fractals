import numpy as np
import matplotlib.pyplot as plt

# Defining the Barnsley fern transformation matrix
transforms = [
    (0, 0, 0, 0.16, 0, 0),
    (0.85, 0.04, -0.04, 0.85, 0, 1.6),
    (0.2, -0.26, 0.23, 0.22, 0, 1.6),
    (-0.15, 0.28, 0.26, 0.24, 0, 0.44)
]

# Define the initial point
x, y = 0, 0

# Generate the Barnsley fern points
n = 100000
points = np.zeros((n, 2))
for i in range(n):
    # Choose a random transformation
    rand = np.random.rand()
    p = None
    if rand < 0.01:
        p = transforms[0]
    elif rand < 0.86:
        p = transforms[1]
    elif rand < 0.93:
        p = transforms[2]
    else:
        p = transforms[3]
    # Apply the transformation to the current point
    x, y = p[0]*x + p[1]*y +p[4], p[2]*x +p[3]*y +p[5]
    points[i, :] = [x, y]

# Plot the Barnsley fern curve
plt.scatter(points[:, 0], points[:, 1], s=0.1, c='green')
plt.axis('off')
plt.show()


