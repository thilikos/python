# Συγχώνευση (fusion) δύο ήδη ταξινομημένων λιστών σε μία ταξινομημένη


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


a = [1, 5, 7, 8, 9]
b = [3, 6, 10, 11, 14]
c = fusion(a, b)
print(c)
