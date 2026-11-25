import math
import random

import matplotlib.pyplot as plt

# Πράξεις τετραγωνικῶν πινάκων.
# Σὲ ΟΛΕΣ τὶς συναρτήσεις οἱ πίνακες εἶναι τετραγωνικοί: n x n (n γραμμές, n στῆλες).


# -------------------------------------------------------- Ἐκτύπωση πίνακα
# Τυπώνει τὸν πίνακα γραμμὴ-γραμμή· τὰ στοιχεῖα κάθε γραμμῆς χωρίζονται μὲ tab.
def print_matrix(M):
    for row in M:
        for x in row:
            print(x, end='\t')     # '\t' = tab: στοιχίζει τὶς στῆλες
        print()                    # ἀλλαγὴ γραμμῆς στὸ τέλος κάθε γραμμῆς
    print()                        # κενὴ γραμμὴ μετὰ τὸν πίνακα


# ------------------------------------------------------ Τυχαῖος πίνακας n x n
# Κάθε στοιχεῖο εἶναι ἕνας τυχαῖος ἀκέραιος ἀπὸ 0 μέχρι q-1.
def random_matrix(n, q):
    M = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = random.randint(0, q - 1)
    return M


# ------------------------------------------------------ Μοναδιαῖος πίνακας n x n
# 1 στὴ διαγώνιο, 0 παντοῦ ἀλλοῦ.
def identity(n):
    I = [[0] * n for i in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I


# -------------------------------------------------------- Ἄθροισμα πινάκων
# Τὸ ἄθροισμα S = A + B γίνεται στοιχεῖο-στοιχεῖο:  S[i][j] = A[i][j] + B[i][j]
def mat_add(A, B):
    n = len(A)
    S = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            S[i][j] = A[i][j] + B[i][j]
    return S


# ------------------------------------------------- Ἀριθμὸς ἐπὶ πίνακα: k·A
# Κάθε στοιχεῖο πολλαπλασιάζεται μὲ τὸν ἀριθμὸ k.
def scalar_mul(k, A):
    n = len(A)
    M = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = k * A[i][j]
    return M


# -------------------------------------------------- Πολλαπλασιασμὸς πινάκων
# Τὸ γινόμενο P = A·B:
#   P[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][n-1]*B[n-1][j]
# δηλαδὴ ἡ γραμμὴ i τοῦ A "ἐπί" τὴ στήλη j τοῦ B.
def mat_mul(A, B):
    n = len(A)
    P = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                P[i][j] += A[i][k] * B[k][j]
    return P


# ------------------------------------------------------------ Δύναμη A^p
# A^p = A·A·...·A (p φορές).  A^0 = I.
def mat_pow(A, p):
    P = identity(len(A))
    for k in range(p):
        P = mat_mul(P, A)
    return P


# ------------------------------- Δύο ἀριθμοὶ μὲ ἄθροισμα τέλειο τετράγωνο
# Δοκιμάζουμε κάθε θέση (i1, j1) μὲ κάθε ΑΛΛΗ θέση (i2, j2).
# Τὸ s εἶναι τέλειο τετράγωνο (0, 1, 4, 9, 16, ...) ἂν ἡ ἀκέραια ῥίζα του
# r = math.isqrt(s) δίνει ξανὰ s ὅταν τὴν ὑψώσουμε στὸ τετράγωνο:  r * r == s.
# Ἐπιστρέφει τὶς δύο θέσεις (i1, j1, i2, j2) ἢ None ἂν δὲν ὑπάρχουν.
def square_pair(M):
    n = len(M)
    for i1 in range(n):
        for j1 in range(n):
            for i2 in range(n):
                for j2 in range(n):
                    if [i1, j1] != [i2, j2]:            # δύο ΔΙΑΦΟΡΕΤΙΚΕΣ θέσεις
                        s = M[i1][j1] + M[i2][j2]
                        r = math.isqrt(s)
                        if r * r == s:
                            return i1, j1, i2, j2
    return None


# ------------------------------------------ Πράξεις μὲ τυχαίους πίνακες
n = 3                            # μέγεθος: n x n
q = 10                           # στοιχεῖα ἀπὸ 0 μέχρι q-1
A = random_matrix(n, q)
B = random_matrix(n, q)
C = random_matrix(n, q)

print('A =')
print_matrix(A)
print('B =')
print_matrix(B)
print('A + B =')
print_matrix(mat_add(A, B))
print('2A =')
print_matrix(scalar_mul(2, A))
print('A·B =')
print_matrix(mat_mul(A, B))
print('B·A =   (γενικὰ ΔΙΑΦΟΡΕΤΙΚΟ: ὁ πολλαπλασιασμὸς πινάκων δὲν εἶναι ἀντιμεταθετικός)')
print_matrix(mat_mul(B, A))
print('A·I =   (ὁ μοναδιαῖος παίζει τὸν ῥόλο τοῦ 1)')
print_matrix(mat_mul(A, identity(n)))
print('A^3 =')
print_matrix(mat_pow(A, 3))

print('Δύο ἀριθμοὶ τοῦ A μὲ ἄθροισμα τέλειο τετράγωνο:')
result = square_pair(A)
if result is None:
    print('δὲν ὑπάρχουν')
else:
    i1, j1, i2, j2 = result
    a = A[i1][j1]
    b = A[i2][j2]
    print(f'A[{i1}][{j1}] + A[{i2}][{j2}] = {a} + {b} = {a + b} = {math.isqrt(a + b)}^2')





