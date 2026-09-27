import math

# Ἔλεγχος ἂν ἕνας θετικὸς ἀριθμὸς εἶναι πρῶτος, μὲ χωριστὴ ἀντιμετώπιση
# τῶν ἀρτίων καὶ τοῦ 2.

r = int(input('Παρακαλῶ δῶστε μου ἕναν ἀριθμό: '))
while r < 1:
    r = int(input('Ὁ ἀριθμὸς ποὺ δώσατε δὲν εἶναι θετικός!\nΠαρακαλῶ δῶστε θετικὸ ἀριθμό: '))

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
