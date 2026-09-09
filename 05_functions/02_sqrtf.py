import math

# Μέθοδος του Ήρωνα για την τετραγωνική ρίζα, κρατώντας όλα τα ενδιάμεσα
# ζεύγη (L, W) στις λίστες x και y.


def my_sqrt2(A, epsilon):
    error = epsilon + 1
    L = A
    W = A / L
    x = [L]
    y = [W]
    while error > epsilon:
        L = (L + W) / 2
        W = A / L
        x.append(L)
        y.append(W)
        error = (L - W) / L
    return L, x, y


def main():
    A = float(input('Δῶσε θετικὸ ἀριθμό: '))
    e = 0.00000000001
    s, x, y = my_sqrt2(A, e)
    error = abs(s - math.sqrt(A))
    print('Ἡ προσέγγιση τῆς τετραγωνικῆς ρίζας τοῦ', A, 'ἰσοῦται μὲ', s)
    print(f'Τὸ σφάλμα τῆς προσέγγισης ἰσοῦται μὲ {error:.5e}')


if __name__ == '__main__':
    main()
