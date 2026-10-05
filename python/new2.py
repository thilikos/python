πλῆθος = 0
n = 2
while πλῆθος < 1000:
    protos = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            protos = False
            break
        d = d + 1
    if protos:
        print(n, end=" ")
        πλῆθος = πλῆθος + 1
    n = n + 1
print()
