# Τυπώνει τοὺς πρώτους 10000 πρώτους ἀριθμούς
# Ἕνας ἀριθμὸς n>1 εἶναι πρῶτος ὅταν δὲν διαιρεῖται μὲ κανέναν
# ἀπὸ τοὺς προηγούμενους πρώτους p μὲ p*p <= n

N = 10000

primes = []
n = 2
while len(primes) < N:
    is_prime = True
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    n = n + 1

for i in range(N):
    print(f'{i+1:5d}: {primes[i]:6d}')
