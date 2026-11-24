import math

import matplotlib.pyplot as plt

# a[r] = True αν ο r+1 είναι πρώτος (το 1 δὲν εἶναι πρῶτος).
# Στη συνέχεια το y κρατά το πλήθος των πρώτων μέχρι κάθε θέση (σωρευτικά).

a = [False, True, True, False]
for r in range(5, 1001):
    i = 3
    c = math.ceil(math.sqrt(r))
    while r % i != 0 and i <= c:
        i += 2
    a.append(i > c and r % 2 == 1)

y = [0, 1]
for i in range(2, len(a)):
    w = y[i - 1]
    if a[i]:
        y.append(w + 1)
    else:
        y.append(w)

# Ἡ λίστα τῶν πρώτων ἀριθμῶν, ξεκινῶντας ἀπὸ τὸ 2.
p = []
for i in range(len(a)):
    if a[i]:
        p.append(i + 1)
print(p)

# plt.plot(y)
# plt.show()
