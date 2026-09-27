import random

import matplotlib.pyplot as plt

# Μέσος ἀριθμὸς βημάτων τυχαίου περιπάτου γιὰ διάφορα μεγέθη τετραγώνου


def random_walk(n):
    x = 0
    y = 0
    sx = [x]
    sy = [y]
    steps = 0
    while abs(x) < n and abs(y) < n:
        r = random.randint(1, 4)
        if r == 1:
            y += 1
        elif r == 2:
            x += 1
        elif r == 3:
            y -= 1
        else:
            x -= 1
        sx.append(x)
        sy.append(y)
        steps += 1
    return steps, sx, sy


st = []
for i in range(40):
    allsteps = 0
    for j in range(2000):
        steps, ax, ay = random_walk(i)
        allsteps += steps
    st.append(allsteps / 2000)

print(st)

plt.plot(st)
plt.show()
