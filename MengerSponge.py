from vpython import *

def menger_sponge(pos, size, depth):
    if depth == 0:
        box(pos=pos, length=size, height=size, width=size)
    else:
        # Divide the box into 27 smaller cubes
        new_size = size / 3
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if abs(x) + abs(y) + abs(z) > 1:
                        new_pos = vector(pos.x + x*new_size, pos.y + y*new_size, pos.z + z*new_size)
                        menger_sponge(new_pos, new_size, depth-1)

# Set up the VPython scene
scene = canvas(width=800, height=600)

# Generate the Menger sponge
pos = vector(0, 0, 0)
size = 200
depth = 3
menger_sponge(pos, size, depth)
