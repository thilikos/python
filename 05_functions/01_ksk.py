# Κόσκινο του Ερατοσθένη, γραμμένο με συναρτήσεις που χρησιμοποιούν
# καθολικές (global) μεταβλητές: z, a, j.


def findnext(j):
    while j < z and a[j] == 0:
        j += 1
    return j


def ellim():
    for i in range(2 * j, z, j):
        a[i] = 0


z = 1000000
a = [0, 0] + list(range(2, z))
j = 0

while j < z:
    j = findnext(j)
    if j < z:
        ellim()
        print(j)
        j += 1

# import matplotlib.pyplot as plt
# plt.plot(a)
# plt.show()
