# Ἔλεγχος ἂν κάθε ἀριθμὸς σὲ ἕνα διάστημα εἶναι πρῶτος

for z in range(1_000_000, 1_100_000):
    isprime = True
    if z % 2 == 0:
        print(z, not isprime)
    else:
        for i in range(3, z // 2 + 1, 2):
            if z % i == 0:
                isprime = False
        print(z, isprime)
