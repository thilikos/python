#!/usr/bin/python
#coding=utf-8

import kondylis, russel, genesis_old_testament

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

#a = lebowski.lebowski_text()
#a = russel.russel_wiki_text()
#a = kondylis.kondylis_text()
a = genesis_old_testament.genesis_old_testament_text()


text = sanitize(a,exclude) #συμβολοσειρά

d = letters_number(text)  #λεξικό: κλειδί=χαρακτήρας, τιμή=πλήθος εμφανίσεων
l = sorted(d.values(),reverse=True) #λίστα: πλήθος εμφανίσεων χαρακτήρων, διατεταγμένο με φθίνουσα σειρά
q= create_list(l,d) #λίστα: q[i]=[πλήθος εμφανίσεων χαρακτήρων, λίστα με χαρακτήρες που έχουν αυτό το πλήθος εμφανίσεων]

words = text.split() #λίστα

dw = letters_number(words) #λεξικό: κλειδί=λεξη, τιμή=πλήθος εμφανίσεων
lw = sorted(dw.values(),reverse=True) #λίστα: πλήθος εμφανίσεων λέξεων, διατεταγμένο με φθίνουσα σειρά
qw=  create_list(lw,dw) #λίστα: q[i]=[πλήθος εμφανίσεων λέξεων,λίστα με λέξεις που έχουν αυτό το πλήθος εμφανίσεων]


print('\n')

print('Ἀριθμὸς χαρακτήρων:',len(text))
print('Ἀριθμὸς πραγματικών χαρακτήρων:',len(d))
print('\n')

for i in q:
    pr= i[0]/float(len(text))*100
    print("%5d"%i[0],"%6.3f"%pr+'%',i[1])
print('\n')

print('Ἀριθμὸς λέξεων:',len(words))
print('Ἀριθμὸς πραγματικών λέξεων:',len(dw))
print('\n')
for i in qw:
    pr= i[0]/float(len(words))*100
    print("%5d"%i[0],"%6.3f"%pr+'%',i[1][0:20])

print('\n')


