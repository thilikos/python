# Ἀκολουθία Fibonacci: ἀναδρομικὰ (fibo2) καὶ ἐπαναληπτικὰ (fibo1).
# Ὁ λόγος διαδοχικῶν ὅρων τείνει στὴ χρυσὴ τομή.
#
# Προσοχή: ἡ fibo2 εἶναι "ἀφελὴς" ἀναδρομὴ καὶ ὁ χρόνος της μεγαλώνει
# ἐκθετικά, γι᾽ αὐτὸ ὁ βρόχος παρακάτω φτάνει μόνο μέχρι τὸ ~30.


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
