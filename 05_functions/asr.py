# Με την εντολή global, η συνάρτηση αλλάζει την καθολική μεταβλητή x.

def func():
    global x
    x = 2


x = 5
func()
print(x)
