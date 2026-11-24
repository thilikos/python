import matplotlib.pyplot as plt

import my_random_walk as myrw

# Ένας τυχαίος περίπατος στο πλέγμα.
# Η random_walk(n) (στο my_random_walk.py) ξεκινά από το (0, 0) και σε κάθε
# βήμα πάει πάνω / δεξιά / κάτω / αριστερά, μέχρι να φτάσει στην άκρη του
# τετραγώνου |x| < n, |y| < n. Επιστρέφει ΔΥΟ λίστες:
#     sx = [x0, x1, x2, ...]   οι τετμημένες όλων των θέσεων
#     sy = [y0, y1, y2, ...]   οι τεταγμένες όλων των θέσεων

n = 100
sx, sy = myrw.random_walk(n)

steps = len(sx) - 1               # η λίστα περιέχει και την αρχική θέση
print(f'Βήματα μέχρι την άκρη: {steps}')
print('Οι 10 πρώτες θέσεις :', list(zip(sx[:10], sy[:10])))
print('Η τελευταία θέση    :', (sx[-1], sy[-1]))
print('Μεγαλύτερο / μικρότερο x:', max(sx), min(sx))
print('Μεγαλύτερο / μικρότερο y:', max(sy), min(sy))

plt.plot([-n, -n, n, n, -n], [-n, n, n, -n, -n], 'r')   # το τετράγωνο
plt.plot(sx, sy, 'b', lw=0.8)                           # η διαδρομή
plt.plot(sx[0], sy[0], 'go')                            # αρχή
plt.plot(sx[-1], sy[-1], 'ro')                          # τέλος
plt.axis('equal')
plt.title(f'Τυχαίος περίπατος: n = {n}, {steps} βήματα')
plt.show()
