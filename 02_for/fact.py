# fact.py -- παραγοντικό με βρόχο for

n = int(input('Δώσε έναν ακέραιο: '))
f = 1
for i in range(1, n + 1):
    f *= i
print('Το παραγοντικό του', n, 'είναι το', f)
