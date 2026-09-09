import math

# Έλεγχος αν ένας θετικός αριθμός είναι πρώτος, με χωριστή αντιμετώπιση
# των αρτίων και του 2.

r = int(input('Παρακαλῶ δῶστε μου ἕναν ἀριθμό: '))
while r < 1:
    r = int(input('Ὀ ἀριθμὸς ποὺ δώσατε δὲν εἶναι θετικός!\nΠαρακαλώ δώστε θετικό αριθμό: '))

if r > 4 and r % 2 == 1:
    i = 3
    c = math.ceil(math.sqrt(r))
    while r % i != 0 and i <= c:
        i += 2
    isprime = i > c
elif r != 2 and r % 2 == 0:
    isprime = False
else:
    isprime = True

print(isprime)
