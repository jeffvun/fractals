import matplotlib.pyplot as plt

def t_square(n, x, y, w):
    if n == 0:
        return
    else:
        plt.plot([x, x+w, x+w, x, x], [y, y, y+w, y+w, y], 'k')
        new_w = w/3
        t_square(n-1, x+new_w, y+new_w, new_w)
        t_square(n-1, x+new_w, y+new_w*4, new_w)
        t_square(n-1, x+new_w*4, y+new_w*4, new_w)
        t_square(n-1, x+new_w*4, y+new_w, new_w)

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')

# Generate the T-Square fractal
n = 5
w = 2**n
t_square(n, 0, 0, w)

# Show the T-Square fractal
plt.show()
