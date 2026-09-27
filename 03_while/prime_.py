import math

import matplotlib.pyplot as plt

# Γιὰ τοὺς περιττοὺς r στὸ [3, z) κρατᾶμε ζεύγη (r, isprime) στὴ λίστα a
# καὶ τὰ σχεδιάζουμε.

z = int(input('Παρακαλῶ δῶσε μου ἕναν ἀριθμό: '))
count = 0
a = []
for r in range(3, z, 2):
    i = 2
    isprime = True
    while i <= math.ceil(math.sqrt(r)):
        if r % i == 0:
            isprime = False
        i += 1
    count += isprime
    a += [r, isprime]

print("Τὸ διάνυσμα εἶναι:", a, "\n ")

b = range(3, len(a) + 3)
plt.plot(b, a)
plt.ylabel('Primes')
plt.xlabel('Numbers')
plt.show()
