import random


st =[]
for n in range(1,50):
    steps = 0
    x= 0
    y= 0
    ax=[x]
    ay=[y]
    while abs(x)<n and abs(y)<n:
        r = random.random()
        if r < 0.25:
            y += 1
        elif r < 0.5:
            x += 1
        elif r < 0.75:
            y -= 1
        else:
            x -= 1
        steps += 1
        ax = ax+[x]
        ay = ay+[y]
    st = st + [steps]
#   print(ax)
#   print(ay)
print(st)



import matplotlib.pyplot as plt


plt.plot(st)
plt.show()


