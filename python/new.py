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




# Σχεδίαση τῆς γραφικῆς παράστασης τοῦ q(x)
import numpy as np
import matplotlib.pyplot as plt

x0 = -b / (3*a)          # σημεῖο καμπῆς, ἐκεῖ ποὺ q''(x)=0
if discriminant > 0:
    w = max(2, 1.5 * abs(r1 - r2))
else:
    w = 3
x = np.linspace(x0 - w, x0 + w, 400)
y = a*x**3 + b*x**2 + c*x + d

plt.plot(x, y, label='q(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
if discriminant > 0:
    plt.plot([r1, r2], [qr1, qr2], 'ro', label='τοπικὰ ἀκρότατα')
plt.title(f'q(x) = {a:.2f}x³ + {b:.2f}x² + {c:.2f}x + {d:.2f}')
plt.xlabel('x')
plt.ylabel('q(x)')
plt.grid(True)
plt.legend()
plt.show()
