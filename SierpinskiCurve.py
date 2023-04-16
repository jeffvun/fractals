import matplotlib.pyplot as plt


def sierpinski_curve(order, length=1):
    if order == 0:
        return [(0, 0), (length, 0)]

    subcurve = sierpinski_curve(order - 1, length / 2)
    result = []
    for a, b in zip(subcurve[:-1], subcurve[1:]):
        result.extend([
            a,
            ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2),
            b
        ])
    return result


if __name__ == '__main__':
    order = 4
    curve = sierpinski_curve(order)
    plt.plot(*zip(*curve), 'k', linewidth=0.5)
    plt.show()
