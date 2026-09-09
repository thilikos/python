import random

def create(n,m):
    b = []
    for i in range(n):
        b += [random.randint(0,m)]
    return b


def shuffle(a):
    import random
    b = []
    i = 1
    n = len(a)
    while i <= n:
        r = random.randint(0,len(a)-1)
        b += [a[r]]
        a=a[0:r]+a[r+1:len(a)]
        i+=1
    return b

