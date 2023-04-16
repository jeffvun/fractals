import matplotlib.pyplot as plt

def terdragon(order):
    """
    Recursive function to generate Terdragon curve of a given order
    """
    if order == 0:
        return [(0, 0), (1, 0)]
    else:
        prev_curve = terdragon(order - 1)
        new_curve = []
        for i in range(len(prev_curve) - 1):
            x1, y1 = prev_curve[i]
            x2, y2 = prev_curve[i+1]
            new_curve.append((x1, y1))
            if x1 == x2:
                if y2 > y1:
                    new_x, new_y = x1 + (y2 - y1) / 2, y1 + (y2 - y1) / 2
                    new_curve.append((new_x, new_y))
                    new_curve.append((new_x, new_y + (x2 - x1) / 2))
                else:
                    new_x, new_y = x1 + (y1 - y2) / 2, y1 - (y1 - y2) / 2
                    new_curve.append((new_x, new_y))
                    new_curve.append((new_x, new_y - (x2 - x1) / 2))
            elif y1 == y2:
                if x2 > x1:
                    new_x, new_y = x1 + (x2 - x1) / 2, y1 + (x2 - x1) / 2
                    new_curve.append((new_x, new_y))
                    new_curve.append((new_x + (y2 - y1) / 2, new_y))
                else:
                    new_x, new_y = x1 - (x1 - x2) / 2, y1 + (x1 - x2) / 2
                    new_curve.append((new_x, new_y))
                    new_curve.append((new_x - (y1 - y2) / 2, new_y))
        new_curve.append(prev_curve[-1])
        return new_curve

# Generate and plot Terdragon curve of order 5
curve = terdragon(5)
x, y = zip(*curve)
plt.plot(x, y, color='blue', linewidth=1)
plt.axis('equal')
plt.show()
