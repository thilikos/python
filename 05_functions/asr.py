# Μὲ τὴν ἐντολὴ global, ἡ συνάρτηση ἀλλάζει τὴν καθολικὴ μεταβλητὴ x.

def func():
    global x
    x = 2


x = 5
func()
print(x)
