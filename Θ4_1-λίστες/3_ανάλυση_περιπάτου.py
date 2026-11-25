import math

import matplotlib.pyplot as plt

import my_random_walk as myrw

# Τί μποροῦμε νὰ μάθουμε ἀπὸ τὶς λίστες sx, sy ἑνὸς περιπάτου;
# Ὅλα τὰ παρακάτω εἶναι ἁπλὲς πράξεις πάνω σὲ λίστες.

n = 200
sx, sy = myrw.random_walk(n)
steps = len(sx) - 1

# 1. Ἡ ἀπόσταση ἀπὸ τὴν ἀρχὴ σὲ κάθε βῆμα: νέα λίστα ἀπὸ δύο παλιὲς (zip)
dist = [math.sqrt(x**2 + y**2) for x, y in zip(sx, sy)]

# 2. Σὲ ποιὰ βήματα ξαναγυρίσαμε στὴν ἀρχὴ (0, 0);
returns = [k for k in range(1, len(sx)) if sx[k] == 0 and sy[k] == 0]

# 3. Πόσες ΔΙΑΦΟΡΕΤΙΚΕΣ θέσεις ἐπισκεφθήκαμε;
#    (Μὲ λίστα: ἐλέγχουμε μὲ "in" ἂν ἔχουμε ξαναδεῖ τὴ θέση. Ἀργὸ γιὰ μεγάλες
#     λίστες -- ἀργότερα θὰ δοῦμε ὅτι τὰ σύνολα (set) τὸ κάνουν πολὺ γρηγορότερα.)
visited = []
for point in zip(sx, sy):
    if point not in visited:
        visited.append(point)

print(f'Βήματα                       : {steps}')
print(f'Μέγιστη ἀπόσταση ἀπὸ τὴν ἀρχή: {max(dist):.2f}')
print(f'Ἐπιστροφὲς στὴν ἀρχή         : {len(returns)}  (στὰ βήματα {returns[:10]} ...)')
print(f'Διαφορετικὲς θέσεις          : {len(visited)}')
print(f'Ποσοστὸ "νέων" βημάτων       : {100 * len(visited) / (steps + 1):.1f}%')

plt.plot(dist, 'b', lw=0.8, label='ἀπόσταση ἀπὸ τὴν ἀρχή')
plt.plot([0, steps], [n, n], 'r--', label='n')
plt.plot([math.sqrt(k) for k in range(steps + 1)], 'g', label='√(βῆμα)')
plt.xlabel('βῆμα')
plt.legend()
plt.show()

 
