import math

# Τυπώνει τους πρώτους 9 αριθμούς της μορφής 2**i - 1 (πρώτοι Mersenne
# και μη): εδώ τυπώνονται όσοι 2**i - 1 είναι πρώτοι.


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
