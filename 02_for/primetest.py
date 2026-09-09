z = int(input("Δῶσε μου ἕναν ἀριθμό: "))

isprime = True
for i in range(2, z):
    if z % i == 0:
        isprime = False

x = '' if isprime else 'δεν'
print('Ὀ ἀριθμὸς', z, x, 'εἶναι πρώτος')
