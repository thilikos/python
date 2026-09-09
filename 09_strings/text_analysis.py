#!/usr/bin/env python3

import kondylis
import russel
import genesis_old_testament

# Ίδια ανάλυση κειμένου με το all.py, σε άλλη πηγή κειμένου.


def how_many_times(text, letter):
    i = 0
    for c in text:
        if c == letter:
            i += 1
    return i  # Ἀριθμὸς


def letters_number(text):  # Χρησιμοποιεῖ τὴν how_many_times
    d = dict()
    for c in set(text):
        d[c] = how_many_times(text, c)
    return d  # Λεξικὸ


def return_keys(lex, value):
    x = []
    for key in lex:
        if lex[key] == value:
            x.append(key)
    return x  # Λίστα


def create_list(values, di):  # Χρησιμοποιεῖ τὴν return_keys
    q = []
    previous = 'NUL'
    for value in values:
        keys = return_keys(di, value)
        if keys != previous:
            q.append([value, keys])
        previous = keys
    return q  # Λίστα (μὲ λίστα μέσα)


def sanitize(a, ex):
    for i in ex:
        a = a.replace(i, ' ')
    return a  # Συμβολοσειρά


exclude = {' ', '·', '–', '-', '"', '(', ')', '.', ',', '[', ']', ':'}  # Χαρακτήρες ποὺ θὰ ἀπαλειφθοῦν

# a = lebowski.lebowski_text()
# a = russel.russel_wiki_text()
# a = kondylis.kondylis_text()
a = genesis_old_testament.genesis_old_testament_text()


text = sanitize(a, exclude)  # συμβολοσειρά

d = letters_number(text)
l = sorted(d.values(), reverse=True)
q = create_list(l, d)

words = text.split()  # λίστα

dw = letters_number(words)
lw = sorted(dw.values(), reverse=True)
qw = create_list(lw, dw)


print('\n')

print('Ἀριθμὸς χαρακτήρων:', len(text))
print('Ἀριθμὸς πραγματικών χαρακτήρων:', len(d))
print('\n')

for i in q:
    pct = i[0] / len(text) * 100
    print("%5d" % i[0], "%6.3f" % pct + '%', i[1])
print('\n')

print('Ἀριθμὸς λέξεων:', len(words))
print('Ἀριθμὸς πραγματικών λέξεων:', len(dw))
print('\n')
for i in qw:
    pct = i[0] / len(words) * 100
    print("%5d" % i[0], "%6.3f" % pct + '%', i[1][0:20])

print('\n')
