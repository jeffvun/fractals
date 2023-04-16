import matplotlib.pyplot as plt

def sierpinski_carpet(order):
    if order == 0:
        return [[1]]
    else:
        smaller_carpet = sierpinski_carpet(order-1)
        n = len(smaller_carpet)
        new_carpet = [[0 for i in range(3*n)] for j in range(3*n)]
        for i in range(n):
            for j in range(n):
                new_carpet[i][j] = smaller_carpet[i][j]
                new_carpet[i][j+n] = smaller_carpet[i][j]
                new_carpet[i][j+2*n] = smaller_carpet[i][j]
                new_carpet[i+n][j] = smaller_carpet[i][j]
                new_carpet[i+n][j+2*n] = smaller_carpet[i][j]
                new_carpet[i+2*n][j] = smaller_carpet[i][j]
                new_carpet[i+2*n][j+n] = smaller_carpet[i][j]
                new_carpet[i+2*n][j+2*n] = smaller_carpet[i][j]
        return new_carpet

order = 4
carpet = sierpinski_carpet(order)
n = len(carpet)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
for i in range(n):
    for j in range(n):
        if carpet[i][j] == 1:
            ax.fill([j/n, (j+1)/n, (j+1)/n, j/n], [1-i/n, 1-i/n, 1-(i+1)/n, 1-(i+1)/n], color='k')

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_aspect('equal')
ax.axis('off')

plt.show()
