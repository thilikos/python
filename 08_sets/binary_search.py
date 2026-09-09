def binary_search(v, key):
    left = 0
    right = len(v)-1
    pos = False
    hit = False
    while left <= right and not hit:
        mid = (left+right)//2
        if v[mid]==key:
            pos = mid
            hit = True
        elif key < v[mid]:
            right = mid-1
        else:
            left = mid+1
    return pos

import shuffle

v = shuffle.create(200,200)
v = shuffle.shuffle(v)

v.sort()
print v

a = binary_search(v,3)
print a

