import random

# Τυχαία ανακάτεμα λίστας με 100 τυχαίες ανταλλαγές θέσεων


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst


n = 100
a = list(range(1, n + 1))

k = 0
while k < 100:
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    a = swap(a, i, j)
    k += 1

print(a)
