import math

def my_sqrt2(A, epsilon):
    error = epsilon+1
    L= A
    W = A/L
    while error>epsilon:
        print(format(L,'20.5f'),"\t",format(W,'20.5f'),"\t",format(L-W,'18.6f'))
        L = (L+W)/2
        W = A/L
        error = (L-W)
    return L

def main():
    import math
    A = float(input('Δώσε θετικό αριθμό: '))
    e = float(input('Δώσε την επιθυμητή ακρίβεια: '))
    s = my_sqrt2(A, e)
    error = abs(s - math.sqrt(A))
    print('H προσέγγιση της τετραγωνικής ρίζας του',A, 'ισούται με', s)
    print('Το σφάλμα της προσέγγισης ισούται με', format(error,'0.15f'),'<',format(e,'0.15f'))

main()