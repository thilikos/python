

def fibo2(a):
    if a <3:
        return a
    else:
        return fibo2(a-1)+fibo2(a-2)






def fibo1(a):
    x1=0
    x2=1
    for i in range(a):
        x = x2
        #       print x
        x2=x1+x2
        x1=x
    return x

for i in range(1,50):
    print(fibo2(i+1)/float(fibo2(i)))



