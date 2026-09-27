#!/usr/bin/env python3

import notes

# Παίρνει ζεύγη λέξεων ἀπὸ τὸ κείμενο notes καὶ ὑπολογίζει τὴν ἀπόσταση
# Hamming (πλῆθος θέσεων ὅπου διαφέρουν) γιὰ κάθε ζεῦγος.


def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


a = notes.notes_text()

words = a.split()  # λίστα
print(words)

m = len(words)
print(m)
for i in range(0, m, 2):
    print(int(10 * ((10 - hamming_distance(words[i], words[i + 1])) * .4)) / 10)
