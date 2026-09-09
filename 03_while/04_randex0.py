import random
x = []
y = []
for i in range(10000):
#   x = x+[100*random.normalvariate(1,1)]
    x = x+[random.randint(1,100)]
#    y = y+[100*random.normalvariate(1,1)]
    y = y+[random.randint(1,100)]
print(x,y,len(x))


import matplotlib.pyplot as plt

plt.plot(x,y,".")
plt.show()
