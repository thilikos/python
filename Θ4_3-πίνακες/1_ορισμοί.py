# Πίνακες (matrices) ὡς λίστες ἀπὸ λίστες
#
# Ἕνας πίνακας r x c (r γραμμές, c στῆλες) ἀποθηκεύεται ὡς μιὰ λίστα μὲ r
# στοιχεῖα, ὅπου κάθε στοιχεῖο εἶναι μιὰ ΓΡΑΜΜΗ: μιὰ λίστα μὲ c ἀριθμούς.
# Τὸ στοιχεῖο στὴ γραμμὴ i καὶ στὴ στήλη j εἶναι τὸ A[i][j]  (i, j ἀπὸ τὸ 0).

A = [[1, 2, 3],
     [4, 5, 6]]                  # πίνακας 2 x 3


def shape(M):
    return len(M), len(M[0])     # (πλῆθος γραμμῶν, πλῆθος στηλῶν)


def print_matrix(M):
    for row in M:
        for x in row:
            print(x, end='\t')     # '\t' = tab: στοιχίζει τὶς στῆλες
        print()
    print()


print('A =')
print_matrix(A)
print('διαστάσεις:', shape(A))
print('A[1][2] =', A[1][2], '  (γραμμὴ 1, στήλη 2)')
print('γραμμὴ 0 :', A[0])                                 # μιὰ γραμμὴ εἶναι λίστα
print('στήλη 1  :', [A[i][1] for i in range(len(A))])     # μιὰ στήλη τὴ "μαζεύουμε"
print()

# ---------------------------------------------- Διάσχιση: δύο ἔνθετοι βρόχοι
rows, cols = shape(A)
for i in range(rows):
    for j in range(cols):
        print(f'A[{i}][{j}] = {A[i][j]}', end='   ')
    print()
print()

# ------------------------------------------------------ Δημιουργία πινάκων
Z = [[0] * 4 for i in range(3)]          # ΣΩΣΤΟ: κάθε γραμμὴ εἶναι ΝΕΑ λίστα
Z[0][0] = 99
print('Z (σωστά):')
print_matrix(Z)



n = 4
I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]       # μοναδιαῖος
print('Μοναδιαῖος πίνακας I:')
print_matrix(I)

T = [[i * j for j in range(1, 10)] for i in range(1, 10)]           # προπαίδεια
print('Ὁ πίνακας τῆς προπαίδειας T[i][j] = (i+1)(j+1):')
print_matrix(T)

# --------------------------------------------- Ἀθροίσματα, μέγιστο, διαγώνιος
M = [[3, 8, 1],
     [4, 6, 2],
     [7, 0, 5]]
print('M =')
print_matrix(M)
print('ἀθροίσματα γραμμῶν:', [sum(row) for row in M])
print('ἀθροίσματα στηλῶν :', [sum(M[i][j] for i in range(3)) for j in range(3)])
print('ἄθροισμα ὅλων    :', sum(sum(row) for row in M))
print('διαγώνιος        :', [M[i][i] for i in range(3)])
print('ἴχνος (trace)    :', sum(M[i][i] for i in range(3)))

best = M[0][0]
best_i, best_j = 0, 0
for i in range(3):
    for j in range(3):
        if M[i][j] > best:
            best = M[i][j]
            best_i, best_j = i, j
print(f'μέγιστο στοιχεῖο  : {best} στὴ θέση ({best_i}, {best_j})')
print()

# ---------------------------------------------------- Ἀνάστροφος (transpose)
# Ἡ γραμμὴ i τοῦ A γίνεται στήλη i τοῦ A^T:  AT[j][i] = A[i][j]
AT = [[0] * rows for j in range(cols)]
for i in range(rows):
    for j in range(cols):
        AT[j][i] = A[i][j]
print('A^T =')
print_matrix(AT)
print()

# Συμμετρικὸς πίνακας: S[i][j] == S[j][i] γιὰ ὅλα τὰ i, j
S = [[2, 1, 0],
     [1, 3, 4],
     [0, 4, 5]]
symmetric = all(S[i][j] == S[j][i] for i in range(3) for j in range(3))
print('Ὁ S εἶναι συμμετρικός;', symmetric)
