import matplotlib.pyplot as plt

def dragon_curve(x, y, n):
    if n == 0:
        return [(x, y)]
    else:
        points = dragon_curve(x, y, n-1)
        new_points = []
        for i in range(len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            dx, dy = x2 - x1, y2 - y1
            new_dx = dy
            new_dy = -dx
            new_x, new_y = x1 + new_dx, y1 + new_dy
            new_points.extend([(x1, y1), (new_x, new_y)])
        new_points.append(points[-1])
        return new_points

# Generate the Dragon curve
n = 15
points = dragon_curve(0, 0, n)

# Plot the Dragon curve
x, y = zip(*points)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, linewidth=1, color='blue')
ax.axis('equal')
ax.axis('off')
plt.show()
