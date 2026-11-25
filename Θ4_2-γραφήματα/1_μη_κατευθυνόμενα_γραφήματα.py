import math

import matplotlib.pyplot as plt

# ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΟ γράφημα G = (V, E): κορυφὲς V καὶ ἀκμὲς E (ζεύγη κορυφῶν).
# Ἡ ἀκμὴ {u, v} δὲν ἔχει φορά: "ἡ u γνωρίζει τὴ v" σημαίνει καὶ "ἡ v γνωρίζει τὴ u".
# Ἀριθμοῦμε τὶς κορυφὲς 0, 1, ..., n-1, ὥστε νὰ τὶς χρησιμοποιοῦμε ὡς ΔΕΙΚΤΕΣ σὲ λίστες.

names = ['Ἄννα', 'Βασίλης', 'Γιῶργος', 'Δήμητρα', 'Ἑλένη', 'Ζωή']   # names[v]
n = len(names)

# ------------------------------------------------- 1. Λίστα ἀκμῶν (edge list)
# Μιὰ λίστα ἀπὸ ζεύγη (λίστες μὲ 2 στοιχεῖα): "ἡ u καὶ ἡ v γνωρίζονται"
edges = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [3, 5], [4, 5]]
print('Κορυφές:', n, '  Ἀκμές:', len(edges))
print()

# --------------------------------------- 2. Λίστες γειτνίασης (adjacency lists)
# adj[v] = ἡ λίστα μὲ τοὺς γείτονες τῆς κορυφῆς v  (μιὰ λίστα ἀπὸ λίστες)
adj = [[] for i in range(n)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)               # μὴ κατευθυνόμενο: ἡ ἀκμὴ μπαίνει καὶ στὶς δύο μεριές

for v in range(n):
    print(f'{v} {names[v]:8} -> {adj[v]}   {[names[u] for u in adj[v]]}')
print()

# ------------------------------------------------------------- 3. Ἐρωτήσεις
deg = [len(adj[v]) for v in range(n)]         # βαθμός = πλῆθος γειτόνων
print('Βαθμοί:', deg)
print('Ἄθροισμα βαθμῶν =', sum(deg), '= 2 x πλῆθος ἀκμῶν =', 2 * len(edges))
print('Ὁ πιὸ "κοινωνικός":', names[deg.index(max(deg))])
print('Γνωρίζονται 0 καὶ 1;', 1 in adj[0])
print('Γνωρίζονται 0 καὶ 5;', 5 in adj[0])

# Κοινοὶ γνωστοὶ δύο κορυφῶν
u, v = 0, 3
common = [w for w in adj[u] if w in adj[v]]
print(f'Κοινοὶ γνωστοὶ τῶν {names[u]} καὶ {names[v]}:', [names[w] for w in common])
















# ------------------------------------------------------------------ 4. Σχέδιο
def draw(names, edges):
    """Ζωγραφίζει τὸ γράφημα: names[v] = ὄνομα τῆς κορυφῆς v, edges = λίστα ἀκμῶν."""
    n = len(names)
    # Βάζουμε τὶς κορυφὲς πάνω σὲ κύκλο: px[v], py[v] εἶναι οἱ συντεταγμένες τῆς v.
    px = [math.cos(2 * math.pi * v / n) for v in range(n)]
    py = [math.sin(2 * math.pi * v / n) for v in range(n)]
    for u, v in edges:
        plt.plot([px[u], px[v]], [py[u], py[v]], 'b')     # ἁπλὴ γραμμή: χωρὶς φορά
    plt.plot(px, py, 'o', ms=25, color='gold')
    for v in range(n):
        plt.text(px[v], py[v], names[v], ha='center', va='center', fontsize=8)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


draw(names, edges)
