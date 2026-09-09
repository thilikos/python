import random

import matplotlib.pyplot as plt

# Για διάφορα μεγέθη τετραγώνου n, μετράμε πόσα βήματα χρειάζεται ένας
# τυχαίος περίπατος για να φτάσει στην άκρη.

st = []
for n in range(1, 50):
    steps = 0
    x = 0
    y = 0
    ax = [x]
    ay = [y]
    while abs(x) < n and abs(y) < n:
        r = random.random()
        if r < 0.25:
            y += 1
        elif r < 0.5:
            x += 1
        elif r < 0.75:
            y -= 1
        else:
            x -= 1
        steps += 1
        ax.append(x)
        ay.append(y)
    st.append(steps)

print(st)

plt.plot(st)
plt.show()
