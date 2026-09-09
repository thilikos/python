import shuffle

def insertion(v):
    for i in range(1,len(v)):
        while i>0 and v[i-1]>v[i]:
            v[i], v[i-1] = v[i-1], v[i]
            print(i,v)
            i -= 1
    return v

x= 20
v = shuffle.create(x,x)

print(v)
print(insertion(v))




v = x*[0]
for i in range(x):
    v[i] = x-i
