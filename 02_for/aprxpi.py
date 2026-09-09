import random

# Προσέγγιση του π με τη μέθοδο Monte Carlo:
# ρίχνουμε n βελάκια στο τετράγωνο [-1, 1] x [-1, 1] και μετράμε
# πόσα πέφτουν μέσα στον εγγεγραμμένο κύκλο ακτίνας 1.

n = 100
hits = 0
for i in range(n):
    # ρίχνω το βελάκι i
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # ελέγχω αν είναι επιτυχία
    if x**2 + y**2 <= 1:
        hits += 1

my_pi = 4 * hits / n
print(my_pi)
