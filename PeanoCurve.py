import numpy as np
import matplotlib.pyplot as plt


def peano_curve(order):
    # Define the base case for the Peano curve
    if order == 0:
        return np.array([[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [1, 2], [1, 3], [0, 3]])

    # Otherwise, recursively define the Peano curve by dividing the plane into 9 squares and
    # applying the Peano curve to each square in a recursive manner
    else:
        subcurve = peano_curve(order - 1)

        left = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]])
        right = np.array([[2.5, -0.5], [3.5, -0.5], [3.5, 0.5], [2.5, 0.5]])
        up = np.array([[-0.5, 2.5], [0.5, 2.5], [0.5, 3.5], [-0.5, 3.5]])
        down = np.array([[-0.5, -3.5], [0.5, -3.5], [0.5, -2.5], [-0.5, -2.5]])

        return np.vstack((
            (subcurve + left) / 3,
            (subcurve + up) / 3,
            (subcurve + right) / 3,
            (subcurve + down) / 3,
            (subcurve + left * 2) / 3
        ))


# Generate and plot the Peano curve of order 4
order = 4
curve = peano_curve(order)
plt.plot(curve[:, 0], curve[:, 1], color='black', linewidth=1)
plt.axis('off')
plt.show()
