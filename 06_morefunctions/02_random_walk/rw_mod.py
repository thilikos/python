import my_random_walk as myrw



def experiment(n=40,m=200):
    st = []
    for i in range(n):
        allsteps = 0
        for j in range(m):
            ax,ay = myrw.random_walk(i)
            allsteps += len(ax)
        st += [allsteps/m]
    return st


st = experiment()

import matplotlib.pyplot as plt
plt.plot(st)
plt.show()


