import matplotlib.pyplot as plt

# Define the function to generate the Cantor Set
def cantor_set(start, end, iterations):
    if iterations == 0:
        return [(start, end)]
    subsegments = cantor_set(start, (2*start+end)/3, iterations-1) + \
                  cantor_set((start+2*end)/3, end, iterations-1)
    return subsegments

# Generate the Cantor Set
segments = cantor_set(0, 1, 5)

# Plot the Cantor Set
fig, ax = plt.subplots()
for segment in segments:
    ax.plot(segment, (0, 0), color='k')
ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 0.1)
ax.axis('off')
plt.show()
