#!/usr/bin/env python3

import notes

# Παίρνει ζεύγη λέξεων από το κείμενο notes και υπολογίζει την απόσταση
# Hamming (πλήθος θέσεων όπου διαφέρουν) για κάθε ζεύγος.


def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


a = notes.notes_text()

words = a.split()  # λίστα
print(words)

m = len(words)
print(m)
for i in range(0, m, 2):
    print(int(10 * ((10 - hamming_distance(words[i], words[i + 1])) * .4)) / 10)
