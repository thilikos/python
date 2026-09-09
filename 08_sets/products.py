# Ξεκινώντας από ένα σύνολο αριθμών, το αντικαθιστούμε επανειλημμένα με το
# σύνολο όλων των γινομένων ζευγών του, και βλέπουμε πόσο γρήγορα μεγαλώνει.


def prods(a):
    x = set()
    for i in a:
        for j in a:
            x.add(i * j)
    return x


def createset(r):
    a = set()
    for i in range(r):
        a.add(i)
    return a


a = createset(4)

x = len(a)
print(a)

for i in range(100):
    x1 = x
    a = prods(a)
    x = len(a)
    print(x / float(x1), len(a))
