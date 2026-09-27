import math

import matplotlib.pyplot as plt

# a[r] = True ἂν ὁ r εἶναι πρῶτος, γιὰ r ἀπὸ 0 ἕως 1000.
# Στὴ συνέχεια τὸ y κρατᾶ τὸ πλῆθος τῶν πρώτων μέχρι κάθε θέση (σωρευτικά).

a = [True, True, True, False]
for r in range(5, 1001):
    i = 3
    c = math.ceil(math.sqrt(r))
    while r % i != 0 and i <= c:
        i += 2
    a.append(i > c and r % 2 == 1)

print("The vector is:", a)

y = [1, 2]
for i in range(2, len(a)):
    w = y[i - 1]
    if a[i]:
        y.append(w + 1)
    else:
        y.append(w)
print(y)

plt.plot(y)
plt.show()
