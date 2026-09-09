import random

import matplotlib.pyplot as plt

# Δύο ανεξάρτητες τυχαίες μεταθέσεις των αριθμών 0..999, σχεδιασμένες σαν σημεία

x = list(range(1000))
random.shuffle(x)
y = list(range(1000))
random.shuffle(y)

plt.plot(x, y, '.')
plt.show()
