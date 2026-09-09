import math

# Προσέγγιση τετραγωνικής ρίζας με τη μέθοδο του Ήρωνα (μέχρι δοσμένη ακρίβεια)


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
    A = float(input('Δώσε θετικό αριθμό: '))
    e = float(input('Δώσε την επιθυμητή ακρίβεια: '))
    s = my_sqrt2(A, e)
    error = abs(s - math.sqrt(A))
    print('H προσέγγιση της τετραγωνικής ρίζας του', A, 'ισούται με', s)
    print(f'Το σφάλμα της προσέγγισης ισούται με {error:.15f} < {e:.15f}')


if __name__ == '__main__':
    main()
