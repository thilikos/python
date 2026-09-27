from random import shuffle

import matplotlib.pyplot as plt

# Ταξινόμηση φυσαλίδας (bubble sort): μετρᾶμε πόσες ἀνταλλαγὲς χρειάζονται
# κατὰ μέσο ὅρο, γιὰ λίστες διαφόρων μεγεθῶν.


def find_illegal_pair(alist):
    i = 0
    while i < len(alist) - 1 and alist[i] < alist[i + 1]:
        i += 1
    return i


def swap(alist, i):
    alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


def bubblesort(alist):
    c = 0
    while True:
        i = find_illegal_pair(alist)
        if i < len(alist) - 1:
            swap(alist, i)
            c += 1
        else:
            break
    return alist, c


repetitions = 10
x = []

for ins in range(50):
    alist = list(range(ins + 1, 0, -1))
    total = 0
    for k in range(repetitions):
        shuffle(alist)
        orderedlist, steps = bubblesort(alist)
        total += steps
    average = total / repetitions
    x.append(average)
print(x)

plt.plot(x)
plt.show()
