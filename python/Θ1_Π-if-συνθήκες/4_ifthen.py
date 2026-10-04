b = float(input('Δῶσε τὸ b: '))
c = float(input('Δῶσε τὸ c: '))
L = float(input('Δῶσε τὸ L: '))
R = float(input('Δῶσε τὸ R: '))
if L > R:
    print('Ἡ τιμὴ τοῦ L πρέπει νὰ μὴν ὑπερβαίνει τὴν τιμὴ τοῦ R')
else:
    xc = -b / 2
    if L <= xc and xc <= R:
        fc = c - (b/2)**2
        print(f'Ἡ μικρότερη τιμὴ τῆς συνάρτησης f στὸ διάστημα [L,R] εἶναι ἡ: {fc:6.3f}')
    else:
        if xc > R:
            fr = R**2 + b*R + c
            print(f'Ἡ μικρότερη τιμὴ τῆς συνάρτησης f στὸ διάστημα [L,R] εἶναι ἡ: {fr:6.3f}')
        else:
            fl = L**2 + b*L + c
            print(f'Ἡ μικρότερη τιμὴ τῆς συνάρτησης f στὸ διάστημα [L,R] εἶναι ἡ: {fl:6.3f}')
