import math

import matplotlib.pyplot as plt

# Για τους περιττούς r στο [3, z) κρατάμε ζεύγη (r, isprime) στη λίστα a
# και τα σχεδιάζουμε.

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

print("Το διάνυσμα είναι:", a, "\n ")

b = range(3, len(a) + 3)
plt.plot(b, a)
plt.ylabel('Primes')
plt.xlabel('Numbers')
plt.show()
