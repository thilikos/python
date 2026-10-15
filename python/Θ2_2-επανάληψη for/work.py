import random

import matplotlib.pyplot as plt




x = []      # οι τετμημένες των σημείων
y = []      # οι τεταγμένες των σημείων
for i in range(100):
    # random.normalvariate(1, 1): κανονική κατανομή με μέση τιμή 1
    # και τυπική απόκλιση 1. Ο πολλαπλασιασμός επί 100 δίνει
    # κανονική κατανομή με μέση τιμή 100 και τυπική απόκλιση 100.
    x.append(100 * random.uniform(0, 1))
    y.append(100 * random.uniform(0, 1))


