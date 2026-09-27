# Ἐλαχιστοποίηση τῆς συνάρτησης f(x) = x^2 + b*x + c στὸ διάστημα [L, R]

b = float(input('Δῶσε τὸ b: '))
c = float(input('Δῶσε τὸ c: '))
L = float(input('Δῶσε τὸ L: '))
R = float(input('Δῶσε τὸ R, μὲ L<R: '))

print(f'Ἐξίσωση: x^2+bx+c, b = {b:.2f} , c = {c:.2f}')
print(f'Διάστημα: [L,R], L = {L:.2f} , R = {R:.2f}')

# Ὑπολογισμὸς κρίσιμου σημείου
xc = -b / 2
if xc < L:
    xmin = L
elif L <= xc <= R:
    xmin = xc
else:
    xmin = R

fmin = xmin**2 + b*xmin + c
print(f'x ἐλαχιστοποίησης = {xmin:.2f}')
print(f'Ἐλάχιστη τιμὴ τῆς f = {fmin:.2f}')
