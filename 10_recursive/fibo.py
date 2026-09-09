# Ακολουθία Fibonacci: αναδρομικά (fibo2) και επαναληπτικά (fibo1).
# Ο λόγος διαδοχικών όρων τείνει στη χρυσή τομή.
#
# Προσοχή: η fibo2 είναι "αφελής" αναδρομή και ο χρόνος της μεγαλώνει
# εκθετικά, γι' αυτό ο βρόχος παρακάτω φτάνει μόνο μέχρι το ~30.


def fibo2(a):
    if a < 3:
        return a
    else:
        return fibo2(a - 1) + fibo2(a - 2)


def fibo1(a):
    x = 0
    x1 = 0
    x2 = 1
    for i in range(a):
        x = x2
        x2 = x1 + x2
        x1 = x
    return x


for i in range(1, 30):
    print(fibo2(i + 1) / fibo2(i))
