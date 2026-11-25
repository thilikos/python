import matplotlib.pyplot as plt

# Γιὰ κάθε r στὸ [3, z) μετρᾶμε πόσους διαιρέτες d ἔχει (πέρα ἀπὸ τὸ 1)
# ἐλέγχοντας ὅλα τὰ i ἀπὸ 2 ἕως r-1.

z = int(input('Please give me a number: '))
count = 0
a = [0, 0, 0]
for r in range(3, z):
    i = 2
    isprime = True
    d = 0
    while i <= r - 1:
        if r % i == 0:
            isprime = False
            d += 1
        i += 1
        count += isprime
    a.append(d)

print("The vector is:", a)

plt.plot(a)
plt.show()
