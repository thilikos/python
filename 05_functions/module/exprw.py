import matplotlib.pyplot as plt

import rwalk

# Χρησιμοποιεῖ τὴ συνάρτηση random_walk ἀπὸ τὸ ξεχωριστὸ module rwalk.py

st = []
for i in range(40):
    allsteps = 0
    for j in range(100):
        steps, ax, ay = rwalk.random_walk(i)
        allsteps += steps
    st.append(allsteps / 100)

print(st)

plt.plot(st)
plt.show()
