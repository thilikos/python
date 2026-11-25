import math

import matplotlib.pyplot as plt

# ΚΑΤΕΥΘΥΝΟΜΕΝΟ γράφημα G = (V, E): κάθε ἀκμὴ εἶναι ΔΙΑΤΕΤΑΓΜΕΝΟ ζεῦγος (u, v),
# δηλαδὴ βέλος u -> v: "ὁ u ἀκολουθεῖ τὸν v". Αὐτὸ ΔΕΝ σημαίνει ὅτι ὁ v ἀκολουθεῖ τὸν u.
# Ἀριθμοῦμε τὶς κορυφὲς 0, 1, ..., n-1, ὥστε νὰ τὶς χρησιμοποιοῦμε ὡς ΔΕΙΚΤΕΣ σὲ λίστες.

names = ['Ἄννα', 'Βασίλης', 'Γιῶργος', 'Δήμητρα', 'Ἑλένη', 'Ζωή']   # names[v]
n = len(names)

# ------------------------------------------------- 1. Λίστα ἀκμῶν (edge list)
# Μιὰ λίστα ἀπὸ ζεύγη (λίστες μὲ 2 στοιχεῖα): [u, v] σημαίνει "ὁ u ἀκολουθεῖ τὸν v"
edges = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 2], [4, 2], [5, 4]]
print('Κορυφές:', n, '  Ἀκμές:', len(edges))
print()

# --------------------------------------- 2. Λίστες γειτνίασης (adjacency lists)
# Τώρα ἔχουμε ΔΥΟ λίστες γειτνίασης:
#   out[v] = ποιοὺς ἀκολουθεῖ ὁ v      (ἐξερχόμενα βέλη v -> ...)
#   inn[v] = ποιοὶ ἀκολουθοῦν τὸν v    (εἰσερχόμενα βέλη ... -> v)
out = [[] for i in range(n)]       # ΠΡΟΣΟΧΗ: ΟΧΙ [[]] * n  (θὰ ἦταν ἡ ΙΔΙΑ λίστα n φορές)
inn = [[] for i in range(n)]       # ('in' εἶναι λέξη-κλειδὶ τῆς Python, γι' αὐτὸ 'inn')
for u, v in edges:
    out[u].append(v)               # ΜΟΝΟ πρὸς τὴ μία μεριά: u -> v
    inn[v].append(u)

for v in range(n):
    print(f'{v} {names[v]:8} ἀκολουθεῖ -> {[names[u] for u in out[v]]}')
print()
for v in range(n):
    print(f'{v} {names[v]:8} τὸν/τὴν ἀκολουθοῦν <- {[names[u] for u in inn[v]]}')
print()

# ------------------------------------------------------------- 3. Ἐρωτήσεις
out_deg = [len(out[v]) for v in range(n)]     # ἔξω-βαθμός = πόσους ἀκολουθεῖ
in_deg = [len(inn[v]) for v in range(n)]      # ἔσω-βαθμός = πόσοι τὸν ἀκολουθοῦν
print('Ἔξω-βαθμοί:', out_deg)
print('Ἔσω-βαθμοί:', in_deg)
print('Ἄθροισμα ἔξω-βαθμῶν =', sum(out_deg), '= ἄθροισμα ἔσω-βαθμῶν =', sum(in_deg),
      '= πλῆθος ἀκμῶν =', len(edges))
print('Ὁ πιὸ "δημοφιλής":', names[in_deg.index(max(in_deg))], 'μὲ', max(in_deg), 'ἀκόλουθους')

# Ἐδῶ ἡ σειρὰ μετράει!
print('Ὁ 0 ἀκολουθεῖ τὸν 1;', 1 in out[0])
print('Ὁ 1 ἀκολουθεῖ τὸν 0;', 0 in out[1])

# Ἀμοιβαῖες ἀκμές: u -> v ΚΑΙ v -> u (κρατᾶμε u < v γιὰ νὰ μὴ μετρηθοῦν δύο φορές)
mutual = [[u, v] for u, v in edges if u < v and u in out[v]]
print('Ἀμοιβαῖα ἀκολουθοῦνται:', [[names[u], names[v]] for u, v in mutual])












# ------------------------------------------------------------------ 4. Σχέδιο
def draw(names, edges):
    """Ζωγραφίζει τὸ κατευθυνόμενο γράφημα: names[v] = ὄνομα τῆς κορυφῆς v,
    edges = λίστα ἀκμῶν [u, v] (βέλος u -> v)."""
    n = len(names)
    # Βάζουμε τὶς κορυφὲς πάνω σὲ κύκλο: px[v], py[v] εἶναι οἱ συντεταγμένες τῆς v.
    px = [math.cos(2 * math.pi * v / n) for v in range(n)]
    py = [math.sin(2 * math.pi * v / n) for v in range(n)]
    for u, v in edges:
        # βέλος ἀπὸ τὴ u στὴ v. Τὸ shrink σταματᾶ τὸ βέλος πρὶν ἀπὸ τὸν κύκλο τῆς κορυφῆς,
        # καὶ τὸ arc3 τὸ καμπυλώνει λίγο, ὥστε τὰ u -> v καὶ v -> u νὰ μὴ συμπίπτουν.
        plt.annotate('', xy=(px[v], py[v]), xytext=(px[u], py[u]),
                     arrowprops=dict(arrowstyle='-|>', color='b', shrinkA=14, shrinkB=14,
                                     mutation_scale=20,        # μέγεθος τῆς μύτης τοῦ βέλους
                                     connectionstyle='arc3,rad=0.15'))
    plt.plot(px, py, 'o', ms=25, color='gold')
    for v in range(n):
        plt.text(px[v], py[v], names[v], ha='center', va='center', fontsize=8)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


draw(names, edges)
