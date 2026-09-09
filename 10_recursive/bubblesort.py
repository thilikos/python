def findillegalpair(alist):
    i = 0
    while i < len(alist)-1 and alist[i] < alist[i+1]:
        i+=1
    return i

def swap(alist,i):
    j=alist[i];
    alist[i]=alist[i+1]
    alist[i+1]=j
    return alist

def bubblesort(alist):
    c=0
    flag = 1
    while flag:
        i = findillegalpair(alist)
        if i < len(alist)-1:
            swap(alist,i)
            c+=1
        else:
            flag = 0
    return alist, c


from random import shuffle

repetitions = 10
x = []

for ins in range(50):
    alist=range(ins+1,0,-1)
    total = 0
    for k in range(repetitions):
        shuffle(alist)
        (orderedlist,steps) = bubblesort(alist)
        total += steps
    average = total/repetitions
    x += [average]
print x


import matplotlib.pyplot as plt
plt.plot(x)
plt.show()
