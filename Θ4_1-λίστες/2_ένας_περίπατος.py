import matplotlib.pyplot as plt

import my_random_walk as myrw

# Ἕνας τυχαῖος περίπατος στὸ πλέγμα.
# Ἡ random_walk(n) (στὸ my_random_walk.py) ξεκινᾶ ἀπὸ τὸ (0, 0) καὶ σὲ κάθε
# βῆμα πάει πάνω / δεξιά / κάτω / ἀριστερά, μέχρι νὰ φτάσει στὴν ἄκρη τοῦ
# τετραγώνου |x| < n, |y| < n. Ἐπιστρέφει ΔΥΟ λίστες:
#     sx = [x0, x1, x2, ...]   οἱ τετμημένες ὅλων τῶν θέσεων
#     sy = [y0, y1, y2, ...]   οἱ τεταγμένες ὅλων τῶν θέσεων

n = 100
sx, sy = myrw.random_walk(n)

steps = len(sx) - 1               # ἡ λίστα περιέχει καὶ τὴν ἀρχικὴ θέση
print(f'Βήματα μέχρι τὴν ἄκρη: {steps}')
print('Οἱ 10 πρῶτες θέσεις :', list(zip(sx[:10], sy[:10])))
print('Ἡ τελευταία θέση    :', (sx[-1], sy[-1]))
print('Μεγαλύτερο / μικρότερο x:', max(sx), min(sx))
print('Μεγαλύτερο / μικρότερο y:', max(sy), min(sy))

plt.plot([-n, -n, n, n, -n], [-n, n, n, -n, -n], 'r')   # τὸ τετράγωνο
plt.plot(sx, sy, 'b', lw=0.8)                           # ἡ διαδρομή
plt.plot(sx[0], sy[0], 'go')                            # ἀρχή
plt.plot(sx[-1], sy[-1], 'ro')                          # τέλος
plt.axis('equal')
plt.title(f'Τυχαῖος περίπατος: n = {n}, {steps} βήματα')
plt.show()
