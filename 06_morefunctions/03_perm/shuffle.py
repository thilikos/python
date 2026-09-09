

def supresszeros(a):
    x = [];
    l = len(a)
    for i in range(l):
        if a[i] > 0:
            x += [a[i]]
    return x

def shuffle(a):
    import random
    b = []
    i = 1
    while i <= n:
        r = random.randint(0,len(a)-1)
        b += [a[r]]
        a[r]=0
        a = supresszeros(a)
        i+=1
    return b

n=100
a = range(1,n+1)
a = shuffle(a)
print(a)

b = range(1,n+1)
b = shuffle(b)
print(b)



import matplotlib.pyplot as plt
plt.plot(a,b)
plt.show()