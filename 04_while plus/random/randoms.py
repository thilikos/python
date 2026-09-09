def random_walk(n):
    import random
    x= 0
    y= 0
    ax=[x]
    ay=[y]
    steps = 0
    #
    while abs(x)<n and abs(y)<n: #
        r = random.random()
        if r < 0.25:
            y += 1
        elif r < 0.5:
            x += 1
        elif r < 0.75:
            y -= 1
        else:
            x -= 1
        steps += 1
        ax = ax+[x]
        ay = ay+[y]
    return steps, ax, ay