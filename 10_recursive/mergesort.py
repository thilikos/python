from random import shuffle

# Ταξινόμηση μὲ συγχώνευση (merge sort), ἀναδρομικά.


def fusion(lefthalf, righthalf):
    i = 0
    j = 0
    k = 0
    fusionlist = (len(lefthalf) + len(righthalf)) * [0]
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            fusionlist[k] = lefthalf[i]
            i += 1
        else:
            fusionlist[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        fusionlist[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        fusionlist[k] = righthalf[j]
        j += 1
        k += 1
    return fusionlist


def merge_sort_short(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        alist = fusion(merge_sort(alist[:mid]), merge_sort(alist[mid:]))
    return alist


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lefthalf = merge_sort(lefthalf)
        righthalf = merge_sort(righthalf)
        return fusion(lefthalf, righthalf)
    else:
        return alist


alist = list(range(1000000))
shuffle(alist)
print(alist)
orderedlist = merge_sort(alist)
print(orderedlist)
