import random

import matplotlib.pyplot as plt

# Νέφος 10000 σημείων μὲ κανονικὴ κατανομὴ στὶς δύο συντεταγμένες

x = []
y = []
for i in range(10000):
    x.append(100 * random.normalvariate(1, 1))
    y.append(100 * random.normalvariate(1, 1))

print(x, y, len(x))

plt.plot(x, y, ".")
plt.show()
