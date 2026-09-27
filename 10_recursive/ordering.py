from random import shuffle

import matplotlib.pyplot as plt

# Σύγκριση merge sort καὶ bubble sort: μετρᾶμε τὸ πλῆθος τῶν βασικῶν
# βημάτων (συγκρίσεις / ἀνταλλαγὲς) γιὰ λίστες διαφόρων μεγεθῶν.


# ====== MERGE =======

def mergesort(alist, p):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lefthalf, p = mergesort(lefthalf, p)
        righthalf, p = mergesort(righthalf, p)
        return fusion(lefthalf, righthalf, p)
    else:
        return alist, p


def fusion(lefthalf, righthalf, p):
    i = 0
    j = 0
    k = 0
    fusionlist = (len(lefthalf) + len(righthalf)) * [0]
    while i < len(lefthalf) and j < len(righthalf):
        p += 1
        if lefthalf[i] < righthalf[j]:
            fusionlist[k] = lefthalf[i]
            i += 1
        else:
            fusionlist[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        fusionlist[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        fusionlist[k] = righthalf[j]
        j += 1
        k += 1
    return fusionlist, p


# ====== BUBBLE =======

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


# ====== ENGINE =======

def countsteps(repetitions, length):
    x1 = []
    x2 = []
    for ins in range(length):
        print(ins)
        alist = list(range(1, ins + 1))[::-1]
        total1 = 0
        total2 = 0
        for k in range(repetitions):
            shuffle(alist)
            orderedlist1, steps1 = mergesort(alist, 0)
            orderedlist2, steps2 = bubblesort(alist)
            total1 += steps1
            total2 += steps2
        average1 = total1 / repetitions
        average2 = total2 / repetitions
        x1.append(average1)
        x2.append(average2)
    return x1, x2


# ====== MAIN =======

repetitions = 1
length = 200

r1, r2 = countsteps(repetitions, length)

plt.plot(r1)
plt.plot(r2)
plt.show()
