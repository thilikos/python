# Ἀνάλυση πολυωνύμου q(x)=ax^3+bx^2+cx+d, a≠0
# Ἕνα πολυώνυμο εἶναι ἁπλὸ ὅταν ὅλες οἱ ρίζες εἶναι διακριτὲς καὶ πραγματικές
# Ἕνα πολυώνυμο εἶναι μονότονο ὅταν εἶναι φθίνουσα ἢ αὔξουσα συνάρτηση
import math

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

