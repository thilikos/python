# Ελαχιστοποίηση της συνάρτησης f(x) = x^2 + b*x + c στο διάστημα [L, R]

b = float(input('Δώσε το b: '))
c = float(input('Δώσε το c: '))
L = float(input('Δώσε το L: '))
R = float(input('Δώσε το R, με L<R: '))

print(f'Εξίσωση: x^2+bx+c, b = {b:.2f} , c = {c:.2f}')
print(f'Διάστημα: [L,R], L = {L:.2f} , R = {R:.2f}')

# Υπολογισμός κρίσιμου σημείου
xc = -b / 2
if xc < L:
    xmin = L
elif L <= xc <= R:
    xmin = xc
else:
    xmin = R

fmin = xmin**2 + b*xmin + c
print(f'x ελαχιστοποίησης = {xmin:.2f}')
print(f'Ελάχιστη τιμή της f = {fmin:.2f}')
