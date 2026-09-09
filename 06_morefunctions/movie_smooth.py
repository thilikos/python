import random

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation

# Κινούμενη εξομάλυνση πολυγώνου με matplotlib.animation


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


def create_random_points(n, m):
    x = []
    y = []
    for i in range(n):
        x.append(float(random.randint(1, m)))
        y.append(float(random.randint(1, m)))
    return x, y


def smooth():
    n = len(x)
    x_new = []
    y_new = []
    for i in range(n - 1):
        x_new.append((x[i] + x[i + 1]) / 2)
        y_new.append((y[i] + y[i + 1]) / 2)
    x_new.append((x[0] + x[n - 1]) / 2)
    y_new.append((y[0] + y[n - 1]) / 2)
    return x_new, y_new


def magnify(d, a=150, m=1):
    for i in range(len(x)):
        d[i] = a + m * (d[i] - a)
    return d


# animation function.  This is called sequentially
def animate(i):
    global x, y, j
    line.set_data(x + [x[0]], y + [y[0]])
    x, y = smooth()
    x = magnify(x, 150, 1.002)
    y = magnify(y, 150, 1.002)
    j += 1
    print(j)
    return line,


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 300), ylim=(0, 300))
line, = ax.plot([], [], lw=1)
j = 0
x, y = create_random_points(n=50, m=300)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1, interval=1, blit=False)
plt.show()
