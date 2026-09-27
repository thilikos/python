# Ξεκινώντας ἀπὸ ἕνα σύνολο ἀριθμῶν, τὸ ἀντικαθιστοῦμε ἐπανειλημμένα μὲ τὸ
# σύνολο ὅλων τῶν γινομένων ζευγῶν του, καὶ βλέπουμε πόσο γρήγορα μεγαλώνει.


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
