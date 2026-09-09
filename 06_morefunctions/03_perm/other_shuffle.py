import random

def swap(l,i,j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
    return l

n = 100
a = range(1,n+1)


k=0
while k < 100:
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)
    a = swap(a,i,j)
    k += 1

print(a)

