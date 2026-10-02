# Ἀνάλυση πολυωνύμου q(x)=ax^3+bx^2+cx+d, a≠0
# Ἕνα πολυώνυμο εἶναι ἁπλὸ ὅταν ὅλες οἱ ρίζες εἶναι διακριτὲς καὶ πραγματικές
# Ἕνα πολυώνυμο εἶναι μονότονο ὅταν εἶναι φθίνουσα ἢ αὔξουσα συνάρτηση
import math

a = float(input('Δῶσε τὸ a: '))
b = float(input('Δῶσε τὸ b: '))
c = float(input('Δῶσε τὸ c: '))
d = float(input('Δῶσε τὸ d: '))

print(f'Τὸ πολυώνυμο εἶναι τὸ {a:6.2f}x^3+{b:6.2f}x^2+{c:6.2f}x+{d:6.2f}')

a1 = a * 3
b1 = b * 2
c1 = c

print(f"Ἡ παράγωγος τοῦ πολυωνύμου εἶναι τὸ q'(x)={a1:6.2f}x^2+{b1:6.2f}x+{c1:6.2f}")

discriminant = b1**2 - 4*a1*c1

print(f"Ἡ διακρίνουσα τῆς παραγώγου τοῦ q'(x) εἶναι {discriminant:6.2f}")

if discriminant <= 0:
    print('Τὸ πολυώνυμο q(x) εἶναι μονότονο καὶ ὄχι ἁπλό')
else:
    print('Τὸ πολυώνυμο q(x) δὲν εἶναι μονότονο')
    r1 = (-b1 + math.sqrt(discriminant)) / (2*a1)
    r2 = (-b1 - math.sqrt(discriminant)) / (2*a1)
    qr1 = a*r1**3 + b*r1**2 + c*r1 + d
    qr2 = a*r2**3 + b*r2**2 + c*r2 + d
    print(f'r1 = {r1:6.2f}, qr1 = {qr1:6.2f},r2 = {r2:6.2f}, qr2 = {qr2:6.2f}  ')
    if qr1*qr2 < 0:
        print('Τὸ πολυώνυμο q(x) εἶναι ἁπλό')
    else:
        print('Τὸ πολυώνυμο q(x) δὲν εἶναι ἁπλό')
