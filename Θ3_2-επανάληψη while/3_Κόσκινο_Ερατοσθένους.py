import matplotlib.pyplot as plt

# Κόσκινο τοῦ Ἐρατοσθένη: a[k] == k ἂν ὁ k εἶναι πρῶτος, ἀλλιῶς a[k] == 0.

z = 100
a = [0, 0] + list(range(2, z + 1))
j = 2
# Ἀρκεῖ νὰ φτάσουμε ὡς τὴ ῥίζα τοῦ z, καὶ τὸ σβήσιμο ἀρχίζει ἀπὸ τὸ j*j:
# τὰ 2j, 3j, ..., (j-1)j τὰ ἔχουν ἤδη σβήσει οἱ μικρότεροι πρῶτοι.
while j * j <= z:
    while j * j <= z and a[j] == 0:
        j += 1
    if j * j <= z:
        for i in range(j * j, z + 1, j):
            a[i] = 0
        j += 1

print(a)

# Φιλτράρισμα: κρατᾶμε μόνο τοὺς μὴ μηδενικούς, δηλαδὴ τοὺς πρώτους.
primes = []
for k in a:
    if k != 0:
        primes.append(k)

print(primes)
print(len(primes))

plt.plot(primes)
plt.show()
