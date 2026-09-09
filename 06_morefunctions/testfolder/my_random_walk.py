def random_walk(n):
    import random
    x= 0
    y= 0
    sx=[x]
    sy=[y]
    while abs(x)<n and abs(y)<n:
        r = random.randint(1,4)
        if r == 1:
            y += 1
        elif r == 2:
            x += 1
        elif r == 3:
            y -= 1
        else:
            x -= 1
        sx += [x]
        sy += [y]
    return sx,sy