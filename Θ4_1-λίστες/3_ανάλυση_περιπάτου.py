import math

import matplotlib.pyplot as plt

import my_random_walk as myrw

# Τι μπορούμε να μάθουμε από τις λίστες sx, sy ενός περιπάτου;
# Όλα τα παρακάτω είναι απλές πράξεις πάνω σε λίστες.

n = 200
sx, sy = myrw.random_walk(n)
steps = len(sx) - 1

# 1. Η απόσταση από την αρχή σε κάθε βήμα: νέα λίστα από δύο παλιές (zip)
dist = [math.sqrt(x**2 + y**2) for x, y in zip(sx, sy)]

# 2. Σε ποια βήματα ξαναγυρίσαμε στην αρχή (0, 0);
returns = [k for k in range(1, len(sx)) if sx[k] == 0 and sy[k] == 0]

# 3. Πόσες ΔΙΑΦΟΡΕΤΙΚΕΣ θέσεις επισκεφθήκαμε;
#    (Με λίστα: ελέγχουμε με "in" αν έχουμε ξαναδεί τη θέση. Αργό για μεγάλες
#     λίστες -- αργότερα θα δούμε ότι τα σύνολα (set) το κάνουν πολύ γρηγορότερα.)
visited = []
for point in zip(sx, sy):
    if point not in visited:
        visited.append(point)

print(f'Βήματα                       : {steps}')
print(f'Μέγιστη απόσταση από την αρχή: {max(dist):.2f}')
print(f'Επιστροφές στην αρχή         : {len(returns)}  (στα βήματα {returns[:10]} ...)')
print(f'Διαφορετικές θέσεις          : {len(visited)}')
print(f'Ποσοστό "νέων" βημάτων       : {100 * len(visited) / (steps + 1):.1f}%')

plt.plot(dist, 'b', lw=0.8, label='απόσταση από την αρχή')
plt.plot([0, steps], [n, n], 'r--', label='n')
plt.plot([math.sqrt(k) for k in range(steps + 1)], 'g', label='√(βήμα)')
plt.xlabel('βήμα')
plt.legend()
plt.show()

 
