# Οἱ 2100 πρῶτοι πρῶτοι ἀριθμοί
N = 2100
plithos = 0   # πόσους πρώτους ἔχουμε βρεῖ
n = 2         # ὁ ὑποψήφιος ἀριθμός
while plithos < N:
    # ἐλέγχουμε ἂν ὁ n διαιρεῖται μὲ κάποιον d, 2 <= d <= √n
    protos = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            protos = False
            break
        d = d + 1
    if protos:
        plithos = plithos + 1
        print(f'{n:6d}', end='')
        if plithos % 10 == 0:   # 10 ἀριθμοὶ ἀνὰ γραμμή
            print()
    n = n + 1
