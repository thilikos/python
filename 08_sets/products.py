import random


def prods(a):
    x = set()
    for i in a:
        for j in a:
            m = i*j
            x.add(m)
    return x


def createset(r):
    a = set()
    for i in range(r):
        a.add(i)
#        a.add(random.randint(1,m))
    return a


a = createset(4)


x=len(a)
print(a)

for i in range(100):
    x1 = x
    a = prods(a)
    x = len(a)
    print(x/float(x1),len(a))



