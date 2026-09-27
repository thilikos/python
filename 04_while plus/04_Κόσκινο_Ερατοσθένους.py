import matplotlib.pyplot as plt

# Κόσκινο τοῦ Ἐρατοσθένη: a[k] == k ἂν ὁ k εἶναι πρῶτος, ἀλλιῶς a[k] == 0.

z = 10000
a = [0, 0] + list(range(2, z))
j = 0
while j < z:
    while j < z and a[j] == 0:
        j += 1
    if j < z:
        for i in range(2 * j, z, j):
            a[i] = 0
        print(j)
        j += 1

# plt.plot(a)
# plt.show()
