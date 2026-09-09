








def fusion(lefthalf,righthalf):
    i=0
    j=0
    k=0
    fusionlist=(len(lefthalf)+len(righthalf))*[0]
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            fusionlist[k]=lefthalf[i]
            i+=1
        else:
            fusionlist[k]=righthalf[j]
            j+=1
        k+=1

    while i < len(lefthalf):
        fusionlist[k]=lefthalf[i]
        i+=1
        k+=1
        
    while j < len(righthalf):
        fusionlist[k]=righthalf[j]
        j+=1
        k+=1
    return fusionlist




def mergeSort_short(alist):
    if len(alist)>1:
        alist=fusion(mergeSort(alist[:len(alist)/2]),mergeSort(alist[len(alist)/2:]))
    return alist



def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)/2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lefthalf = mergeSort(lefthalf)
        righthalf = mergeSort(righthalf)
        return fusion(lefthalf,righthalf)
    else:
        return alist



from random import shuffle
alist=range(1000000)
shuffle(alist)
print(alist)
orderedlist = mergeSort(alist)
print(orderedlist)


