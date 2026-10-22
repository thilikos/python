import matplotlib.pyplot as plt

# Κόσκινο του Ερατοσθένη: a[k] == k αν ο k είναι πρώτος, αλλιώς a[k] == 0.

z = 100
a = [0, 0] + list(range(2, z + 1))
j = 2
# Αρκεί να φτάσουμε ως τη ρίζα του z, και το σβήσιμο αρχίζει από το j*j:
# τα 2j, 3j, ..., (j-1)j τα έχουν ήδη σβήσει οι μικρότεροι πρώτοι.

while j * j <= z:
    while j * j <= z and a[j] == 0:
        j += 1
    if j * j <= z:
            for i in range(j * j, z + 1, j):
                a[i] = 0
            j += 1

maxn = 0

i = 2
while i<=z:
    j = 0 
    while i+j<=z and a[i+j]==0:
        j += 1
    maxn = max(j,maxn)
    i = i+j+1

print(maxn)


     