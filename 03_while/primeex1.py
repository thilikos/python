import math

import matplotlib.pyplot as plt

# Συλλογὴ τῶν πρώτων ἀριθμῶν στὸ [3, z) καὶ σχεδίασή τους

z = int(input('Please give me a number: '))
a = []
for r in range(3, z, 2):
    i = 2
    isprime = True
    while i <= math.ceil(math.sqrt(r)):
        if r % i == 0:
            isprime = False
        i += 1
    if isprime:
        a.append(r)

print("The vector is:", a)

plt.plot(a)
plt.show()
