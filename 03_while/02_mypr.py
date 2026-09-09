import math

r = int(input('Please give me a number: '))
isprime = True
i = 2
while (i <= math.ceil(math.sqrt(r))):
    if r%i==0 and r !=2 :
        isprime = False
    i+=1
print(isprime)







