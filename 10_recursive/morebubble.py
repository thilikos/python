import sys
from random import shuffle

sys.setrecursionlimit(1000000)

# Ταξινόμηση φυσαλίδας, γραμμένη και επαναληπτικά (bubblesort) και
# αναδρομικά (recbubble).


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


def recbubble(alist):
    if find_illegal_pair(alist) < len(alist) - 1:
        alist = recbubble(swap(alist, find_illegal_pair(alist)))
    return alist


data = list(range(300))
shuffle(data)
newlist = recbubble(data)
print(newlist)
