import random
n = 100
hits = 0
for i in range(n):
    # ρίχνω το βελάκι i
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    # ελέγχω αν είναι επιτυχία
    if x**2 + y**2 <= 1:
        hits += 1
myPi = 4*hits/n
print(myPi)