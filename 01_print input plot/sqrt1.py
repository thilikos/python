import math

# Προσέγγιση τετραγωνικῆς ρίζας μὲ τὴ μέθοδο τοῦ Ἥρωνα (σταθερὸ πλῆθος βημάτων)


def my_sqrt(A, steps):
    L = A
    W = A / L
    for _ in range(steps):
        L = (L + W) / 2
        W = A / L
    return L


a = 10_000_000_000
builtin = math.sqrt(a)
print('The result is:', format(my_sqrt(a, 21), '20.15f'), format(builtin, '20.15f'))
