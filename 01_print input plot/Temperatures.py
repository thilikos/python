#   Temperatures.py
#   Author: Alan Richmond, Python3.codes

import matplotlib.pyplot as plt

#   Range of scales between freezing and boiling water
F = [32, 212]                   # Fahrenheit
C = [0, 100]                    # Centigrade

plt.title('Convert Centigrade / Fahrenheit')
plt.ylabel('degrees Centigrade')
plt.xlabel('degrees Fahrenheit')
plt.xlim(32, 212)              # try commenting this out...
plt.grid(True)

plt.plot(F, C)
plt.show()
