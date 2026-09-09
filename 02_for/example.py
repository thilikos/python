z = int(input("Δῶσε μου ἕναν ἀριθμό: "))

isprime = True
if z != 2:
    if z % 2 != 0:
        for i in range(3, z, 2):
            if z % i == 0:
                isprime = False
                print(i)
    else:
        isprime = False

print(isprime)
