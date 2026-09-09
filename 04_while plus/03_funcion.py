import math

sty = []
stx = []
for i in range(-2000,2000):
    if i != 0:
        x = i/10000.
        stx = stx + [x]
        y = math.cos(.1/x)
        sty = sty + [y]



import matplotlib.pyplot as plt

plt.plot(stx,sty)
plt.show()


