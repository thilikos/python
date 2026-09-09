def linear_search(v, key):
    loc = 0
    pos = False
    hit = False
    while loc < len(v) and not hit:
        if v[loc]==key:
            pos = loc
            hit = True
        else:
            loc += 1
    return pos


import shuffle

v = shuffle.create(20,2)
print v

a = linear_search(v,3)
print a