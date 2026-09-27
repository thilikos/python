import math

# Τυπώνει τοὺς πρώτους 9 ἀριθμοὺς τῆς μορφῆς 2**i - 1 (πρῶτοι Mersenne
# καὶ μή): ἐδῶ τυπώνονται ὅσοι 2**i - 1 εἶναι πρῶτοι.


def is_prime(r):
    result = True
    i = 2
    while i <= math.ceil(math.sqrt(r)):
        if r % i == 0 and r != 2:
            result = False
        i += 1
    return result


found = 1
i = 2
while found < 10:
    if is_prime(2**i - 1):
        print(2**i - 1)
        found += 1
    i += 1
