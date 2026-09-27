import math

# Προσέγγιση τετραγωνικῆς ρίζας μὲ τὴ μέθοδο τοῦ Ἥρωνα (μέχρι δοσμένη ἀκρίβεια)


def my_sqrt2(A, epsilon):
    error = epsilon + 1
    L = A
    W = A / L
    while error > epsilon:
        print(f'{L:20.5f}\t{W:20.5f}\t{L - W:18.6f}')
        L = (L + W) / 2
        W = A / L
        error = L - W
    return L


def main():
    A = float(input('Δῶσε θετικὸ ἀριθμό: '))
    e = float(input('Δῶσε τὴν ἐπιθυμητὴ ἀκρίβεια: '))
    s = my_sqrt2(A, e)
    error = abs(s - math.sqrt(A))
    print('Ἡ προσέγγιση τῆς τετραγωνικῆς ρίζας τοῦ', A, 'ἰσοῦται μὲ', s)
    print(f'Τὸ σφάλμα τῆς προσέγγισης ἰσοῦται μὲ {error:.15f} < {e:.15f}')


if __name__ == '__main__':
    main()
