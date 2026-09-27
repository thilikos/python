import random

# Προσέγγιση τοῦ π μὲ τὴ μέθοδο Monte Carlo:
# ρίχνουμε n βελάκια στὸ τετράγωνο [-1, 1] x [-1, 1] καὶ μετρᾶμε
# πόσα πέφτουν μέσα στὸν ἐγγεγραμμένο κύκλο ἀκτίνας 1.

n = 100
hits = 0
for i in range(n):
    # ρίχνω τὸ βελάκι i
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # ἐλέγχω ἂν εἶναι ἐπιτυχία
    if x**2 + y**2 <= 1:
        hits += 1

my_pi = 4 * hits / n
print(my_pi)
