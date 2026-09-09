import random


def create(n, m):
    b = []
    for i in range(n):
        b.append(random.randint(0, m))
    return b


def shuffle(a):
    b = []
    i = 1
    n = len(a)
    while i <= n:
        r = random.randint(0, len(a) - 1)
        b.append(a[r])
        a = a[:r] + a[r + 1:]
        i += 1
    return b
