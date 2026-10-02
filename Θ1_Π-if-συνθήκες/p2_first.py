a = float(input('Παρακαλῶ δῶστε τὸ a: '))
b = float(input('Εὐχαριστῶ! Παρακαλῶ δῶστε τὸ b: '))
if a > b:
    print(f'Τὸ a={a:6.2f} εἶναι μεγαλύτερο τοῦ b={b:6.2f}')
else:
    if a < b:
        print(f'Τὸ a={a:6.2f} εἶναι μικρότερο τοῦ b={b:6.2f}')
    else:
        print(f'Τὸ a={a:6.2f} εἶναι ἴσο τοῦ b={b:6.2f}')
