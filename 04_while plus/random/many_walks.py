

import randoms

import matplotlib.pyplot as plt


for r in range(10):
    (z,x,y) = randoms.random_walk(100)
    plt.plot(x[0],y[0],"x")
    plt.plot(x[z],y[z],"o")
    plt.plot(x,y)
    plt.ylabel('X')
    plt.xlabel('Y')
    plt.show()

#print(random_walk(100))
#main()