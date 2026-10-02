a = float(input('Παρακαλῶ, δῶστε τὸ a: '))
print(f'a = {a}')
b = float(input('Παρακαλῶ, δῶστε τὸ b: '))
print(f'b = {b}')

max = ((a + b) + abs(a - b)) / 2
min = ((a + b) - abs(a - b)) / 2
print(f'τὸ μικρότερο ἀπὸ τὰ a καὶ b εἶναι τό:{int(min):3d}\n'
      f' καὶ τὸ μεγαλύτερο ἀπὸ τὰ a καὶ b εἶναι τό:{int(max):3d}')
