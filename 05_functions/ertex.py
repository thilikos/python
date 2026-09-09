x = 50  # καθολική μεταβλητή

def func():
#    global x
#    print('Το x είναι', x)
    x=2
    print('Άλλαξα το τοπικό x σε', x)

func()
print('Το x είναι ακόμα', x)