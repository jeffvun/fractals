import matplotlib.pyplot as plt

def dragon_curve(n):
    if n == 0:
        return [(0, 0), (1, 0)]
    else:
        prev_points = dragon_curve(n-1)
        new_points = []
        for i in range(len(prev_points)-1):
            x1, y1 = prev_points[i]
            x2, y2 = prev_points[i+1]
            dx, dy = x2 - x1, y2 - y1
            if i % 2 == 0:
                new_dx = dy
                new_dy = -dx
            else:
                new_dx = -dy
                new_dy = dx
            new_x, new_y = x1 + dx/2 + new_dx/2, y1 + dy/2 + new_dy/2
            new_points.extend([(x1, y1), (new_x, new_y)])
        new_points.append((1, 0))
        return new_points

# Generate the Dragon Curve fractal
n = 12
points = dragon_curve(n)

# Plot the Dragon Curve fractal
x, y = zip(*points)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, linewidth=1, color='blue')
ax.axis('equal')
ax.axis('off')
plt.show()
