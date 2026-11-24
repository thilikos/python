import math

import matplotlib.pyplot as plt

# ΚΑΤΕΥΘΥΝΟΜΕΝΟ γράφημα G = (V, E): κάθε ακμή είναι ΔΙΑΤΕΤΑΓΜΕΝΟ ζεύγος (u, v),
# δηλαδή βέλος u -> v: "ο u ακολουθεί τον v". Αυτό ΔΕΝ σημαίνει ότι ο v ακολουθεί τον u.
# Αριθμούμε τις κορυφές 0, 1, ..., n-1, ώστε να τις χρησιμοποιούμε ως ΔΕΙΚΤΕΣ σε λίστες.

names = ['Άννα', 'Βασίλης', 'Γιώργος', 'Δήμητρα', 'Ελένη', 'Ζωή']   # names[v]
n = len(names)

# ------------------------------------------------- 1. Λίστα ακμών (edge list)
# Μια λίστα από ζεύγη (λίστες με 2 στοιχεία): [u, v] σημαίνει "ο u ακολουθεί τον v"
edges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 2], [4, 2], [5, 4]]
print('Κορυφές:', n, '  Ακμές:', len(edges))
print()

# --------------------------------------- 2. Λίστες γειτνίασης (adjacency lists)
# Τώρα έχουμε ΔΥΟ λίστες γειτνίασης:
#   out[v] = ποιους ακολουθεί ο v      (εξερχόμενα βέλη v -> ...)
#   inn[v] = ποιοι ακολουθούν τον v    (εισερχόμενα βέλη ... -> v)
out = [[] for i in range(n)]       # ΠΡΟΣΟΧΗ: ΟΧΙ [[]] * n  (θα ήταν η ΙΔΙΑ λίστα n φορές)
inn = [[] for i in range(n)]       # ('in' είναι λέξη-κλειδί της Python, γι' αυτό 'inn')
for u, v in edges:
    out[u].append(v)               # ΜΟΝΟ προς τη μία μεριά: u -> v
    inn[v].append(u)

for v in range(n):
    print(f'{v} {names[v]:8} ακολουθεί -> {[names[u] for u in out[v]]}')
print()
for v in range(n):
    print(f'{v} {names[v]:8} τον/την ακολουθούν <- {[names[u] for u in inn[v]]}')
print()

# ------------------------------------------------------------- 3. Ερωτήσεις
out_deg = [len(out[v]) for v in range(n)]     # έξω-βαθμός = πόσους ακολουθεί
in_deg = [len(inn[v]) for v in range(n)]      # έσω-βαθμός = πόσοι τον ακολουθούν
print('Έξω-βαθμοί:', out_deg)
print('Έσω-βαθμοί:', in_deg)
print('Άθροισμα έξω-βαθμών =', sum(out_deg), '= άθροισμα έσω-βαθμών =', sum(in_deg),
      '= πλήθος ακμών =', len(edges))
print('Ο πιο "δημοφιλής":', names[in_deg.index(max(in_deg))], 'με', max(in_deg), 'ακόλουθους')

# Εδώ η σειρά μετράει!
print('Ο 0 ακολουθεί τον 1;', 1 in out[0])
print('Ο 1 ακολουθεί τον 0;', 0 in out[1])

# Αμοιβαίες ακμές: u -> v ΚΑΙ v -> u (κρατάμε u < v για να μη μετρηθούν δύο φορές)
mutual = [[u, v] for u, v in edges if u < v and u in out[v]]
print('Αμοιβαία ακολουθούνται:', [[names[u], names[v]] for u, v in mutual])












# ------------------------------------------------------------------ 4. Σχέδιο
def draw(names, edges):
    """Ζωγραφίζει το κατευθυνόμενο γράφημα: names[v] = όνομα της κορυφής v,
    edges = λίστα ακμών [u, v] (βέλος u -> v)."""
    n = len(names)
    # Βάζουμε τις κορυφές πάνω σε κύκλο: px[v], py[v] είναι οι συντεταγμένες της v.
    px = [math.cos(2 * math.pi * v / n) for v in range(n)]
    py = [math.sin(2 * math.pi * v / n) for v in range(n)]
    for u, v in edges:
        # βέλος από τη u στη v. Το shrink σταματά το βέλος πριν από τον κύκλο της κορυφής,
        # και το arc3 το καμπυλώνει λίγο, ώστε τα u -> v και v -> u να μη συμπίπτουν.
        plt.annotate('', xy=(px[v], py[v]), xytext=(px[u], py[u]),
                     arrowprops=dict(arrowstyle='-|>', color='b', shrinkA=14, shrinkB=14,
                                     mutation_scale=20,        # μέγεθος της μύτης του βέλους
                                     connectionstyle='arc3,rad=0.15'))
    plt.plot(px, py, 'o', ms=25, color='gold')
    for v in range(n):
        plt.text(px[v], py[v], names[v], ha='center', va='center', fontsize=8)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


draw(names, edges)
