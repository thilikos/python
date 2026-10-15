import random
import matplotlib.pyplot as plt


x = []      # οι τετμημένες των σημείων
y = []      # οι τεταγμένες των σημείων



for i in range(10):
    # και τυπική απόκλιση 1. Ο πολλαπλασιασμός επί 100 δίνει
    # κανονική κατανομή με μέση τιμή 100 και τυπική απόκλιση 100.
    x += [100 * random.uniform(0,1)]
    y += [100 * random.uniform(0,1)]


print(x, y, len(x))









