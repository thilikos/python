import random

import matplotlib.pyplot as plt

# Τυχαία μετάθεση: διαλέγουμε επανειλημμένα ένα τυχαίο στοιχείο, το βάζουμε
# στο αποτέλεσμα και το αφαιρούμε από τη λίστα.


def suppress_zeros(a):
    return [v for v in a if v > 0]


def shuffle(a):
    b = []
    i = 1
    while i <= n:
        r = random.randint(0, len(a) - 1)
        b.append(a[r])
        a[r] = 0
        a = suppress_zeros(a)
        i += 1
    return b


n = 100
a = shuffle(list(range(1, n + 1)))
print(a)

b = shuffle(list(range(1, n + 1)))
print(b)

plt.plot(a, b)
plt.show()
