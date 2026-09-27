import matplotlib.pyplot as plt

# Μέθοδος τοῦ Ἥρωνα, μὲ γραφικὴ ἀναπαράσταση: γιὰ κάθε βῆμα σχεδιάζουμε
# ἕνα ὀρθογώνιο μὲ πλευρὲς τὶς τρέχουσες τιμὲς L καὶ W.


def my_sqrt2(A, epsilon):
    error = epsilon + 1
    L = A
    W = A / L
    x = [L]
    y = [W]
    while error > epsilon:
        L = (L + W) / 2
        W = A / L
        x.append(L)
        y.append(W)
        error = (L - W) / L
    return L, x, y


def square(x, y, z, w):
    a1 = x - z / 2
    b1 = y - w / 2
    a2 = x + z / 2
    b2 = y + w / 2
    plt.plot([a1, a1, a2, a2, a1], [b1, b2, b2, b1, b1])


A = float(input('Give positive number: '))
e = 0.00000000001
s, x, y = my_sqrt2(A, e)
print(len(x))

square(0, 0, A, A)
for i in range(len(x)):
    square(0, 0, x[i], y[i])
plt.show()
