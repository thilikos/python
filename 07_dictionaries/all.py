import math, random
import primes as pr

def isprime(r):
    isp = True
    i=3
    if r % 2  == 1 or r==2:
        while (i <= math.ceil(math.sqrt(r))):
            if r%i==0 and r !=2 :
                isp = False
            i+=2
    else: isp = False
    return isp

def sumofdigits(a):
    x = 0
    for i  in range(int(math.ceil(math.log(a+1,10)))):
        x += a//(10**i)-(a//(10**(i+1)))*10
    return x

def recursive_sumofdigits(a):
    while a>9:
        a = sumofdigits(a)
    return a

def which_numbers(d,t):
    h = []
    for i in primes_sums:
        if primes_sums[i] == t:
            h += [i]
    return h


primes_sums = dict()


x = 10**8

#for i in range(2,x):
#    if isprime(i):
#        primes_sums[i]=recursive_sumofdigits(i)

p = pr.giveprimes(x)

for y in range(len(p)):
    primes_sums[p[y]]=recursive_sumofdigits(p[y])


print(x)
s = float(len(primes_sums))
max = 0
for i in range(1,10):
    l = len(which_numbers(primes_sums,i))
    if max<l:
        max = l
        intmax  = i
    pr = l/s*100
    print(i,"%6d"%l,"%8.4f"%pr,"%")
print("And the winner is",intmax)









