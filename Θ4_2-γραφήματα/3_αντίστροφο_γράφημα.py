import math
import random

import matplotlib.pyplot as plt

# Ἕνα κατευθυνόμενο γράφημα μὲ κορυφὲς 0, 1, ..., n-1:
#   - ΛΙΣΤΑ ΑΚΜΩΝ:        edges = [[u, v], ...], κάθε [u, v] εἶναι ἕνα βέλος u -> v
#   - ΛΙΣΤΕΣ ΓΕΙΤΝΙΑΣΗΣ:  adj[u] = ἡ λίστα μὲ τὶς κορυφὲς v γιὰ τὶς ὁποῖες ὑπάρχει βέλος u -> v
# Τὸ ΑΝΤΙΣΤΡΟΦΟ γράφημα ἔχει τὶς ἴδιες κορυφὲς καὶ τὰ ἴδια βέλη, ἀλλὰ ἀνάποδα:
# γιὰ κάθε βέλος u -> v τοῦ ἀρχικοῦ, ἔχει τὸ βέλος v -> u.

def random_edges(n, prob):
    """1. Τυχαῖο κατευθυνόμενο γράφημα μὲ n κορυφές, ὡς λίστα ἀκμῶν:
    κάθε βέλος u -> v (u != v) ὑπάρχει μὲ πιθανότητα prob."""
    edges = []
    for u in range(n):
        for v in range(n):
            if u != v and random.random() < prob:
                edges.append([u, v])
    return edges


def adjacency_lists(n, edges):
    """2. Ἀπὸ τὴ λίστα ἀκμῶν φτιάχνει τὶς λίστες γειτνίασης."""
    adj = [[] for i in range(n)]       # ΠΡΟΣΟΧΗ: ΟΧΙ [[]] * n
    for u, v in edges:
        adj[u].append(v)               # βέλος u -> v: ἡ v μπαίνει στὴ λίστα τῆς u
    return adj


def reverse(adj):
    """3. Ἐπιστρέφει τὶς λίστες γειτνίασης τοῦ ἀντίστροφου γραφήματος."""
    n = len(adj)
    rev = [[] for i in range(n)]
    for u in range(n):
        for v in adj[u]:               # βέλος u -> v στὸ ἀρχικό ...
            rev[v].append(u)           # ... γίνεται βέλος v -> u στὸ ἀντίστροφο
    return rev


def print_graphs(adj, rev):
    """4. Τυπώνει δίπλα-δίπλα τὶς λίστες γειτνίασης τοῦ ἀρχικοῦ καὶ τοῦ ἀντίστροφου."""
    print(f'   {"Ἀρχικό":30} Ἀντίστροφο')
    for u in range(len(adj)):
        left = f'{u} -> {adj[u]}'
        print(f'   {left:30} {u} -> {rev[u]}')
    print()


n = 1000
edges = random_edges(n, 0.0001)
g = adjacency_lists(n, edges)
r = reverse(g)

print('Λίστα ἀκμῶν:', edges)
print()
print_graphs(g, r)

# Ἔλεγχος: ἂν ἀντιστρέψουμε δύο φορές, παίρνουμε πίσω τὸ ἀρχικό
# (μὲ sorted, γιατὶ ἡ σειρὰ μέσα σὲ κάθε λίστα μπορεῖ νὰ διαφέρει)
print('reverse(reverse(g)) == g ;', [sorted(a) for a in reverse(r)] == [sorted(a) for a in g])





























def draw(adj, title):
    """Ζωγραφίζει τὸ γράφημα μὲ τὶς κορυφὲς πάνω σὲ κύκλο."""
    n = len(adj)
    px = [math.cos(2 * math.pi * v / n) for v in range(n)]
    py = [math.sin(2 * math.pi * v / n) for v in range(n)]
    for u in range(n):
        for v in adj[u]:
            plt.annotate('', xy=(px[v], py[v]), xytext=(px[u], py[u]),
                         arrowprops=dict(arrowstyle='->', color='b', shrinkA=12, shrinkB=12,
                                         connectionstyle='arc3,rad=0.15'))  # γιὰ νὰ μὴ συμπίπτουν u->v καὶ v->u
    plt.plot(px, py, 'o', ms=20, color='gold')
    for v in range(n):
        plt.text(px[v], py[v], str(v), ha='center', va='center')
    plt.title(title)
    plt.axis('equal')
    plt.axis('off')





plt.subplot(1, 2, 1)                   # 1 γραμμή, 2 στῆλες, 1ο σχῆμα
draw(g, 'Ἀρχικὸ γράφημα')
plt.subplot(1, 2, 2)                   # 2ο σχῆμα
draw(r, 'Ἀντίστροφο γράφημα')
plt.show()

























