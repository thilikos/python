import math

import matplotlib.pyplot as plt

# ΜΗ ΚΑΤΕΥΘΥΝΟΜΕΝΟ γράφημα G = (V, E): κορυφές V και ακμές E (ζεύγη κορυφών).
# Η ακμή {u, v} δεν έχει φορά: "η u γνωρίζει τη v" σημαίνει και "η v γνωρίζει τη u".
# Αριθμούμε τις κορυφές 0, 1, ..., n-1, ώστε να τις χρησιμοποιούμε ως ΔΕΙΚΤΕΣ σε λίστες.

names = ['Άννα', 'Βασίλης', 'Γιώργος', 'Δήμητρα', 'Ελένη', 'Ζωή']   # names[v]
n = len(names)

# ------------------------------------------------- 1. Λίστα ακμών (edge list)
# Μια λίστα από ζεύγη (λίστες με 2 στοιχεία): "η u και η v γνωρίζονται"
edges = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [3, 5], [4, 5]]
print('Κορυφές:', n, '  Ακμές:', len(edges))
print()

# --------------------------------------- 2. Λίστες γειτνίασης (adjacency lists)
# adj[v] = η λίστα με τους γείτονες της κορυφής v  (μια λίστα από λίστες)
adj = [[] for i in range(n)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)               # μη κατευθυνόμενο: η ακμή μπαίνει και στις δύο μεριές

for v in range(n):
    print(f'{v} {names[v]:8} -> {adj[v]}   {[names[u] for u in adj[v]]}')
print()

# ------------------------------------------------------------- 3. Ερωτήσεις
deg = [len(adj[v]) for v in range(n)]         # βαθμός = πλήθος γειτόνων
print('Βαθμοί:', deg)
print('Άθροισμα βαθμών =', sum(deg), '= 2 x πλήθος ακμών =', 2 * len(edges))
print('Ο πιο "κοινωνικός":', names[deg.index(max(deg))])
print('Γνωρίζονται 0 και 1;', 1 in adj[0])
print('Γνωρίζονται 0 και 5;', 5 in adj[0])

# Κοινοί γνωστοί δύο κορυφών
u, v = 0, 3
common = [w for w in adj[u] if w in adj[v]]
print(f'Κοινοί γνωστοί των {names[u]} και {names[v]}:', [names[w] for w in common])
















# ------------------------------------------------------------------ 4. Σχέδιο
def draw(names, edges):
    """Ζωγραφίζει το γράφημα: names[v] = όνομα της κορυφής v, edges = λίστα ακμών."""
    n = len(names)
    # Βάζουμε τις κορυφές πάνω σε κύκλο: px[v], py[v] είναι οι συντεταγμένες της v.
    px = [math.cos(2 * math.pi * v / n) for v in range(n)]
    py = [math.sin(2 * math.pi * v / n) for v in range(n)]
    for u, v in edges:
        plt.plot([px[u], px[v]], [py[u], py[v]], 'b')     # απλή γραμμή: χωρίς φορά
    plt.plot(px, py, 'o', ms=25, color='gold')
    for v in range(n):
        plt.text(px[v], py[v], names[v], ha='center', va='center', fontsize=8)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


draw(names, edges)
