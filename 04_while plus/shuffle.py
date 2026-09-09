    import matplotlib.pyplot as plt
import random



x = range(1000)
random.shuffle(x)
y = range(1000)
random.shuffle(y)
#print(a)

plt.plot(x,y,'.')
plt.show()
