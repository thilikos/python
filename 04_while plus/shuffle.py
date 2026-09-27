import random

import matplotlib.pyplot as plt

# Δύο ἀνεξάρτητες τυχαῖες μεταθέσεις τῶν ἀριθμῶν 0..999, σχεδιασμένες σὰν σημεῖα

x = list(range(1000))
random.shuffle(x)
y = list(range(1000))
random.shuffle(y)

plt.plot(x, y, '.')
plt.show()
