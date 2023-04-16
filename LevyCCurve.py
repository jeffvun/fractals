import matplotlib.pyplot as plt

def levy_c_curve(order, length):
    if order == 0:
        # base case
        return [(0, 0), (length, 0)]
    else:
        # recursive case
        # get the previous curve
        prev_curve = levy_c_curve(order - 1, length)
        # compute the new points
        x0, y0 = prev_curve[0]
        xn, yn = prev_curve[-1]
        x_new = (x0 + xn + (y0 - yn)) / 2
        y_new = (y0 + yn + (xn - x0)) / 2
        # return the new curve
        return levy_c_curve(order - 1, length)[:-1] + \
               levy_c_curve(order - 1, length)[::-1] + \
               [(x_new, y_new)] + \
               levy_c_curve(order - 1, length)[1:]

# test the function
order = 10
length = 100
curve = levy_c_curve(order, length)

# plot the curve
fig, ax = plt.subplots()
ax.plot([x for x, y in curve], [y for x, y in curve], 'k')
ax.set_aspect('equal')
plt.show()
