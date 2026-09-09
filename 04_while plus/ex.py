z= 1000000000

a = [0,0]+range(2,z)

j=0

while j<z:
    while j<z and a[j] == 0:
        j += 1
    if j<z:
        for i in range(2*j,z,j):
            a[i] = 0
        print(j)
        j = j+1



