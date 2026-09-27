import random

import matplotlib.pyplot as plt

# Ἐξομάλυνση πολυγώνου: κάθε νέα κορυφὴ εἶναι τὸ μέσο δύο διαδοχικῶν.
# Οἱ συναρτήσεις smooth() καὶ plot() δουλεύουν μὲ τὶς καθολικὲς λίστες x, y.


def create_random_points(n=50, m=200):
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


def plot(r):
    x1 = x + [x[0]]
    y1 = y + [y[0]]
    plt.plot([0, r + 1, r + 1, 0, 0], [0, 0, r + 1, r + 1, 0])
    plt.plot(x1, y1)
    plt.show()


points = 30
size = 100

x, y = create_random_points(points, size)
i = 0
while i < 9:
    i += 1
    x, y = smooth()
    plot(size)
