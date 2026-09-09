def random_walk(n):
    import random
    x = 0
    y = 0
    sx = [x]
    sy = [y]
    steps = 0
    while abs(x)<n and abs(y)<n:
        r = random.randint(1,4)
        if r == 1:
            y += 1
        elif r == 2:
            x += 1
        elif r == 3:
            y -= 1
        else:
            x -= 1
        sx += [x]
        sy += [y]
        steps += 1
    return steps,sx,sy




p =  4000

st = []
for i in range(20):
    allsteps = 0
    for j in range(p):
        steps,ax,ay = random_walk(i)
        allsteps += steps
    st += [allsteps/p]



print(st)




import matplotlib.pyplot as plt
plt.plot(st)
plt.show()
