# Ὑπολογισμὸς ἐμβαδοῦ καὶ ὄγκου τόρου!
import math
import numpy as np
import matplotlib.pyplot as plt

R = int(input('Παρακαλῶ, δῶστε τὴν μεγάλη ἀκτίνα (ἀκέραιος): '))
print(f'R = {R}')
r = float(input('Παρακαλῶ, δῶστε τὴν μικρὴ ἀκτίνα: '))
print(f'r = {r}')

A = 4*math.pi**2*R*r
print(f'A = {A}')
V = 2*math.pi**2*R*r**2
print(f'V = {V}')

z = 'Θεώρημα τοῦ Πάππου'
print(f'{z}:\n Ὁ τόρος μὲ "μεγάλη ἀκτίνα" R= {R:12d} καὶ \'μικρὴ ἀκτίνα\' r = {r:10.4e}\n'
      f'ἔχει ἐπιφάνεια A = {A:20.8f} καὶ ὄγκο V = {V:20.7f}')






# Σχεδίαση τοῦ τόρου!
u, v = np.meshgrid(np.linspace(0, 2*np.pi, 60), np.linspace(0, 2*np.pi, 30))
X = (R + r*np.cos(v))*np.cos(u)
Y = (R + r*np.cos(v))*np.sin(u)
Z = r*np.sin(v)

ax = plt.figure().add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_aspect('equal')
#ax.set_zticks([-r, 0, r])
#ax.set_title(f'Τόρος: R = {R}, r = {r}')
plt.show()
