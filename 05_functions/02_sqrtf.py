def my_sqrt2(A, epsilon):
    error = epsilon+1
    L= A
    W = A/L
    x = [L]
    y = [W]
    while error>epsilon:
        L = (L+W)/2
        W = A/L
        x += [L]
        y += [W]
        error = (L-W)/L
    return L,x,y


def main():
    import math
    A = float(input('Δῶσε θετικὸ ἀριθμό: '))
    #    e = float(input('Δῶσε τὴν ἐπιθυμητὴ ἀκρίβεια: '))
    e = 0.00000000001
    s,x,y = my_sqrt2(A, e)
    error = abs(s - math.sqrt(A))
    print('Ἡ προσέγγιση τῆς τετραγωνικῆς ρίζας τοῦ', A, 'ἰσοῦται μὲ', s)
    print('Τὸ σφάλμα τῆς προσέγγισης ἰσοῦται μὲ', format(error,'.5e'))

main()