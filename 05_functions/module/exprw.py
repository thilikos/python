import rwalk


st = []
for i in range(40):
    allsteps = 0
    for j in range(100):
        steps,ax,ay = rwalk.random_walk(i)
        allsteps += steps
    st += [allsteps/100]

print(st)


#print(steps)

import matplotlib.pyplot as plt
plt.plot(st)
plt.show()


