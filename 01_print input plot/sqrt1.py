import math

def my_sqrt(A, steps):
    L= A
    W = A/L
    for i in range(steps):
        L = (L+W)/2
        W = A/L
    return L

a = 10000000000
st2 = math.sqrt(a);
print('The results is:',format(my_sqrt(a,21),'20.15f'),format(st2,'20.15f'))