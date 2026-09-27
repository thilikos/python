import matplotlib.pyplot as plt

import my_random_walk as myrw

# Πείραμα: μέσο μῆκος τυχαίου περιπάτου γιὰ μεγέθη τετραγώνου 0..n-1


def experiment(n=40, m=200):
    st = []
    for i in range(n):
        allsteps = 0
        for j in range(m):
            ax, ay = myrw.random_walk(i)
            allsteps += len(ax)
        st.append(allsteps / m)
    return st


st = experiment()

plt.plot(st)
plt.show()
