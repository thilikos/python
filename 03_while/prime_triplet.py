import math
def isprime(r):
    isprime = True
    i = 2
    while (i <= math.ceil(math.sqrt(r))):
        if r%i==0 and r !=2 :
            isprime = False
        i+=1
    return isprime


x=1
i=2
while x<10:
    if isprime(2**i-1):
        print(2**i-1)
        x+=1
    i+=1



