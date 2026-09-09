import math
import random
import matplotlib.pyplot as plt

def create_random_points(n=50,m=200):
    x=[]
    y=[]
    for i in range(n):
        x += [float(random.randint(1,m))]
        y += [float(random.randint(1,m))]
    return x,y

def smooth():
    n = len(x)
    xNew = []
    yNew = []
    for i in range(n-1):
        xNew += [(x[i]+x[i+1])/2]
        yNew += [(y[i]+y[i+1])/2]
    xNew += [(x[0]+x[n-1])/2]
    yNew += [(y[0]+y[n-1])/2]
    return xNew,yNew

def plot(r):
    x1 = x+[x[0]]
    y1 = y+[y[0]]
    plt.plot([0,r+1,r+1,0,0],[0,0,r+1,r+1,0])
    plt.plot(x1,y1)
    plt.show()


points = 30
size = 100

x,y=create_random_points(points,size)
i=0
while i<9:
    i+=1
    x,y = smooth()
    plot(size)
