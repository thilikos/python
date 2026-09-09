import matplotlib.pyplot as plt

# Για κάθε r στο [3, z) μετράμε πόσους διαιρέτες d έχει (πέρα από το 1)
# ελέγχοντας όλα τα i από 2 έως r-1.

z = int(input('Please give me a number: '))
count = 0
a = [0, 0, 0]
for r in range(3, z):
    i = 2
    isprime = True
    d = 0
    while i <= r - 1:
        if r % i == 0:
            isprime = False
            d += 1
        i += 1
        count += isprime
    a.append(d)

print("The vector is:", a)

plt.plot(a)
plt.show()
