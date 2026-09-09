
import math

a = [True,True,True,False]
for r in range(5,1001):
    i=3
    c= math.ceil(math.sqrt(r))
    while r%i!=0 and i <= c:
        i=i+2
    a = a + [i>c and r%2 == 1]

print("The vector is:",a)


y = [1,2]
for i in range(2,len(a)):
    w = y[i-1]
    if a[i]:
        y = y + [w+1]
    else:
        y = y +[w]
print(y)

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.plot(y)
plt.show()