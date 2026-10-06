# Βρίσκει τὰ πρῶτα 10 ζεύγη φίλιων ἀριθμῶν
# Δύο διαφορετικοὶ ἀριθμοὶ a, b εἶναι φίλιοι ὅταν s(a)=b καὶ s(b)=a,
# ὅπου s(n) τὸ ἄθροισμα τῶν γνήσιων διαιρετῶν τοῦ n

def s(n):
    # Οἱ διαιρέτες ἔρχονται σὲ ζεύγη d καὶ n//d, ἀρκεῖ νὰ ψάξουμε ὡς τὴ √n
    total = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            total = total + d
            if d != n // d:
                total = total + n // d
        d = d + 1
    return total

N = 10

count = 0
a = 2
while count < N:
    b = s(a)
    # b > a: κάθε ζεῦγος τὸ τυπώνουμε μία φορά, καὶ ἀποκλείουμε τοὺς τέλειους (b = a)
    if b > a and s(b) == a:
        count = count + 1
        print(f'{count:2d}: {a:6d} καὶ {b:6d}')
    a = a + 1
