import numpy as np
import matplotlib.pyplot as plt

def hilbert_curve(order, angle=90):
    if order == 0:
        return np.array([0, 0])

    step = 2 ** (order - 1)
    prev_curve = hilbert_curve(order - 1, angle=-angle)
    prev_curve = np.vstack([prev_curve, np.zeros(prev_curve.shape)])

    new_curve = np.copy(prev_curve)

    new_curve[:, 0] = prev_curve[:, 1]
    new_curve[:, 1] = prev_curve[:, 0]

    if angle == 90:
        new_curve[:, 1] *= -1
        new_curve[:, 1] += step
    else:
        new_curve[:, 0] *= -1
        new_curve[:, 0] += step

    return new_curve

order = 4
curve = hilbert_curve(order)

plt.plot(curve[:, 0], curve[:, 1])
plt.show()
