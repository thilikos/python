import sys
sys.setrecursionlimit(1000000)

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

def recbubble(list):
    if findillegalpair(list) < len(list)-1:
        list = recbubble(swap(list,findillegalpair(list)))
    return list


from random import shuffle


list = range(300)
shuffle(list)
newlist=recbubble(list)
print(newlist)



