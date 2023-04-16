import matplotlib.pyplot as plt

def cantor_dust(n, x_min, x_max, y_min, y_max):
    if n == 0:
        return [(x_min, y_min, x_max - x_min, y_max - y_min)]
    else:
        width = (x_max - x_min) / 3.0
        rect1 = cantor_dust(n - 1, x_min, x_min + width, y_min, y_max)
        rect2 = cantor_dust(n - 1, x_max - width, x_max, y_min, y_max)
        return rect1 + rect2

n = 5
rects = cantor_dust(n, 0, 1, 0, 1)

fig, ax = plt.subplots()
for rect in rects:
    x, y, width, height = rect
    ax.add_patch(plt.Rectangle((x, y), width, height, facecolor='black'))

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_aspect('equal')
ax.axis('off')
plt.show()
