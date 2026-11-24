import math
import matplotlib.pyplot as plt

err = float(input('Δῶστε τὸ σφάλμα: '))

n = 2
e = err + 1

while e > err:
    n = n + 1
    A_n = (n/2)*math.sin(2*math.pi/n)
    B_n = n*math.tan(math.pi/n)
    rho_n = (A_n + B_n)/2
    e = B_n - A_n

print(f'n = {n}')
print(f'rho_n = {rho_n}')










R = 1/math.cos(math.pi/n)

xa, ya = [], []
xb, yb = [], []
for k in range(n + 1):
    theta = 2*math.pi*k/n
    xa.append(math.cos(theta))
    ya.append(math.sin(theta))
    xb.append(R*math.cos(theta + math.pi/n))
    yb.append(R*math.sin(theta + math.pi/n))

xc, yc = [], []
for k in range(201):
    theta = 2*math.pi*k/200
    xc.append(math.cos(theta))
    yc.append(math.sin(theta))

plt.plot(xc, yc, 'k--', label='κύκλος: π')
plt.plot(xa, ya, 'b-', label=f'ἐγγεγραμμένο: A_n = {A_n:.6f}')
plt.plot(xb, yb, 'r-', label=f'περιγεγραμμένο: B_n = {B_n:.6f}')
plt.gca().set_aspect('equal')
plt.title(f'n = {n},  rho_n = {rho_n:.6f}')
plt.legend()
plt.show()
