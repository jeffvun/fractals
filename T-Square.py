import matplotlib.pyplot as plt

def t_square(x, y, size, n):
    if n == 0:
        return [(x, y)]
    else:
        points = t_square(x, y, size/3, n-1)
        new_points = []
        for i in range(len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            dx, dy = x2 - x1, y2 - y1
            new_dx = dy
            new_dy = -dx
            new_x1, new_y1 = x1 + dx/3, y1 + dy/3
            new_x2, new_y2 = x2 - dx/3, y2 - dy/3
            new_x, new_y = new_x1 + new_dx/3, new_y1 + new_dy/3
            new_points.extend([(x1, y1), (new_x1, new_y1), (new_x, new_y), (new_x2, new_y2)])
        new_points.append(points[-1])
        return new_points

# Generate the T-Square fractal
n = 5
points = t_square(0, 0, 100, n)

# Plot the T-Square fractal
x, y = zip(*points)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, linewidth=1, color='blue')
ax.axis('equal')
ax.axis('off')
plt.show()
