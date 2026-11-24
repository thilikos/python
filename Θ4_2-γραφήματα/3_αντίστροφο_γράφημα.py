import math
import random

import matplotlib.pyplot as plt

# Ένα κατευθυνόμενο γράφημα με κορυφές 0, 1, ..., n-1:
#   - ΛΙΣΤΑ ΑΚΜΩΝ:        edges = [[u, v], ...], κάθε [u, v] είναι ένα βέλος u -> v
#   - ΛΙΣΤΕΣ ΓΕΙΤΝΙΑΣΗΣ:  adj[u] = η λίστα με τις κορυφές v για τις οποίες υπάρχει βέλος u -> v
# Το ΑΝΤΙΣΤΡΟΦΟ γράφημα έχει τις ίδιες κορυφές και τα ίδια βέλη, αλλά ανάποδα:
# για κάθε βέλος u -> v του αρχικού, έχει το βέλος v -> u.

def random_edges(n, prob):
    """1. Τυχαίο κατευθυνόμενο γράφημα με n κορυφές, ως λίστα ακμών:
    κάθε βέλος u -> v (u != v) υπάρχει με πιθανότητα prob."""
    edges = []
    for u in range(n):
        for v in range(n):
            if u != v and random.random() < prob:
                edges.append([u, v])
    return edges


def adjacency_lists(n, edges):
    """2. Από τη λίστα ακμών φτιάχνει τις λίστες γειτνίασης."""
    adj = [[] for i in range(n)]       # ΠΡΟΣΟΧΗ: ΟΧΙ [[]] * n
    for u, v in edges:
        adj[u].append(v)               # βέλος u -> v: η v μπαίνει στη λίστα της u
    return adj


def reverse(adj):
    """3. Επιστρέφει τις λίστες γειτνίασης του αντίστροφου γραφήματος."""
    n = len(adj)
    rev = [[] for i in range(n)]
    for u in range(n):
        for v in adj[u]:               # βέλος u -> v στο αρχικό ...
            rev[v].append(u)           # ... γίνεται βέλος v -> u στο αντίστροφο
    return rev


def print_graphs(adj, rev):
    """4. Τυπώνει δίπλα-δίπλα τις λίστες γειτνίασης του αρχικού και του αντίστροφου."""
    print(f'   {"Αρχικό":30} Αντίστροφο')
    for u in range(len(adj)):
        left = f'{u} -> {adj[u]}'
        print(f'   {left:30} {u} -> {rev[u]}')
    print()


n = 1000
edges = random_edges(n, 0.0001)
g = adjacency_lists(n, edges)
r = reverse(g)

print('Λίστα ακμών:', edges)
print()
print_graphs(g, r)

# Έλεγχος: αν αντιστρέψουμε δύο φορές, παίρνουμε πίσω το αρχικό
# (με sorted, γιατί η σειρά μέσα σε κάθε λίστα μπορεί να διαφέρει)
print('reverse(reverse(g)) == g ;', [sorted(a) for a in reverse(r)] == [sorted(a) for a in g])





























def draw(adj, title):
    """Ζωγραφίζει το γράφημα με τις κορυφές πάνω σε κύκλο."""
    n = len(adj)
    px = [math.cos(2 * math.pi * v / n) for v in range(n)]
    py = [math.sin(2 * math.pi * v / n) for v in range(n)]
    for u in range(n):
        for v in adj[u]:
            plt.annotate('', xy=(px[v], py[v]), xytext=(px[u], py[u]),
                         arrowprops=dict(arrowstyle='->', color='b', shrinkA=12, shrinkB=12,
                                         connectionstyle='arc3,rad=0.15'))  # για να μη συμπίπτουν u->v και v->u
    plt.plot(px, py, 'o', ms=20, color='gold')
    for v in range(n):
        plt.text(px[v], py[v], str(v), ha='center', va='center')
    plt.title(title)
    plt.axis('equal')
    plt.axis('off')





plt.subplot(1, 2, 1)                   # 1 γραμμή, 2 στήλες, 1ο σχήμα
draw(g, 'Αρχικό γράφημα')
plt.subplot(1, 2, 2)                   # 2ο σχήμα
draw(r, 'Αντίστροφο γράφημα')
plt.show()

























