import sys

# Παραγοντικὸ μὲ ἀναδρομή. Τὸ factorial(1000) χρειάζεται βάθος ἀναδρομῆς
# ~1000, γι᾽ αὐτὸ ἀνεβάζουμε τὸ ὅριο.
sys.setrecursionlimit(5000)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(1000))
