import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians

def pythagoras_tree(n, L, theta, x0, y0, color='g'):
    if n == 0:
        return
    x1 = x0 + L * cos(radians(theta))
    y1 = y0 + L * sin(radians(theta))
    x2 = x1 + L * cos(radians(theta-90))
    y2 = y1 + L * sin(radians(theta-90))
    x3 = x0 + L * cos(radians(theta-90))
    y3 = y0 + L * sin(radians(theta-90))
    plt.fill([x0, x1, x2, x3], [y0, y1, y2, y3], color=color)
    pythagoras_tree(n-1, L/np.sqrt(2), theta-45, x2, y2, color=color)
    pythagoras_tree(n-1, L/np.sqrt(2), theta+45, x1, y1, color=color)

# Example usage
fig, ax = plt.subplots(figsize=(6, 6))
pythagoras_tree(8, 1, 0, 0, 0)
ax.axis('off')
plt.show()
