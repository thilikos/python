import sys

# Παραγοντικό με αναδρομή. Το factorial(1000) χρειάζεται βάθος αναδρομής
# ~1000, γι' αυτό ανεβάζουμε το όριο.
sys.setrecursionlimit(5000)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(1000))
