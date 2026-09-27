import math

import primes as pr

# Ἴδιο μὲ τὸ all.py, ἀλλὰ γιὰ μικρὸ x (10**3), κατάλληλο γιὰ ἐπίδειξη.


def sum_of_digits(a):
    x = 0
    for i in range(int(math.ceil(math.log(a + 1, 10)))):
        x += a // (10**i) - (a // (10**(i + 1))) * 10
    return x


def recursive_sum_of_digits(a):
    while a > 9:
        a = sum_of_digits(a)
    return a


def which_numbers(d, t):
    return [i for i in d if d[i] == t]


primes_sums = {}

x = 10**3

p = pr.giveprimes(x)
for prime in p:
    primes_sums[prime] = recursive_sum_of_digits(prime)

s = float(len(primes_sums))
best_count = 0
best_digit = None
for i in range(1, 10):
    count = len(which_numbers(primes_sums, i))
    if best_count < count:
        best_count = count
        best_digit = i
    pct = count / s * 100
    print(i, "%6d" % count, "%8.4f" % pct, "%")
print("And the winner is", best_digit)
