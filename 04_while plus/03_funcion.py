import math

import matplotlib.pyplot as plt

# Γράφημα της f(x) = cos(0.1 / x) κοντά στο 0, όπου ταλαντώνεται πολύ γρήγορα

sty = []
stx = []
for i in range(-2000, 2000):
    if i != 0:
        x = i / 10000
        stx.append(x)
        y = math.cos(0.1 / x)
        sty.append(y)

plt.plot(stx, sty)
plt.show()
