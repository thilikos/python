import matplotlib.pyplot as plt

import randoms

# Σχεδιάζει 10 τυχαίους περιπάτους, τὸν καθένα σὲ ξεχωριστὸ γράφημα

for r in range(10):
    steps, x, y = randoms.random_walk(100)
    plt.plot(x[0], y[0], "x")
    plt.plot(x[steps], y[steps], "o")
    plt.plot(x, y)
    plt.ylabel('X')
    plt.xlabel('Y')
    plt.show()
