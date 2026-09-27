# fact.py -- παραγοντικὸ μὲ βρόχο for

n = int(input('Δῶσε ἕναν ἀκέραιο: '))
f = 1
for i in range(1, n + 1):
    f *= i
print('Τὸ παραγοντικὸ τοῦ', n, 'εἶναι τὸ', f)
