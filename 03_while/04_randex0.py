import random

import matplotlib.pyplot as plt

# Νέφος 10000 σημείων με ακέραιες συντεταγμένες στο [1, 100]

x = []
y = []
for i in range(10000):
    x.append(random.randint(1, 100))
    y.append(random.randint(1, 100))

print(x, y, len(x))

plt.plot(x, y, ".")
plt.show()
