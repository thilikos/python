for z in range(1000000,1100000):
    isprime = True
    if z%2 == 0:
        print(z,not isprime)
    else:
        for i in range(3,int(z/2)+1,2):
            if z%i == 0:
                isprime = False
        print(z,isprime)

