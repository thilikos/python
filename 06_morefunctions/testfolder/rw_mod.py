import my_random_walk as rdw

def experiment(n=40,m=200):
    st = []
    for i in range(n):
        allsteps = 0
        for j in range(m):
            ax,ay = rdw.random_walk(i)
            allsteps += len(ax)
        st += [allsteps/m]
    return st


st = experiment()

import matplotlib.pyplot as plt
plt.plot(st)
plt.show()


