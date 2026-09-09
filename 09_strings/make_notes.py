#!/usr/bin/python
#coding=utf-8

import notes

def how_many_times(text,letter):
    i=0
    for c in text:
        if c == letter:
            i+=1
    return i # Ἀριθμὸς

def letters_number(text):  # Χρησιμοποιεῖ τὴν set_of_text καὶ τὴν how_many_times
    d = dict()
    for c in set(text):
        d[c]=how_many_times(text,c)
    return d # Λεξικὸ

def return_keys(lex,value):
    x = []
    for i in lex.keys():
        if lex[i] == value:
            x+=[i]
    return x # Λίστα

def create_list(list,di): # Χρησιμοποιεῖ τὴν return_keys
    q=[]
    a1 = 'NUL'
    for x in list:
        a = return_keys(di,x)
        if a != a1:
            q += [[x,a]]
        a1 = a
    return q # Λίστα (μὲ λίστα μέσα)

def sanitize(a,ex):
    for i in ex:
        a = a.replace(i,' ')
    return a # Συμβολοσειρά


exclude={' ','·','–','-','"','(',')','.',',','[',']',':'} # Χαρακτήρες ποὺ θὰ ἀπαλειφθοῦν


def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1,ch2 in zip(s1,s2))


#a = lebowski.lebowski_text()
#a = russel.russel_wiki_text()
#a = kondylis.kondylis_text()
#a = genesis_old_testament.genesis_old_testament_text()
a = notes.notes_text()




words = a.split() #λίστα

print(words)

m=len(words)
print(m)
for i in range(0,m,2):
    print(int(10*((10-hamming_distance(words[i],words[i+1]))*.4))/10)
          



