import kondylis
import russel
import lebowski
import genesis_old_testament

# Ἀνάλυση κειμένου: μετρᾶμε πόσο συχνὰ ἐμφανίζεται κάθε χαρακτῆρας καὶ
# κάθε λέξη, καὶ τὰ τυπώνουμε ταξινομημένα κατὰ φθίνουσα συχνότητα.


def how_many_times(text, letter):
    i = 0
    for c in text:
        if c == letter:
            i += 1
    return i  # Ἀριθμός


def letters_number(text):  # Χρησιμοποιεῖ τὴν how_many_times
    d = dict()
    for c in set(text):
        d[c] = how_many_times(text, c)
    return d  # Λεξικό


def return_keys(lex, value):
    x = []
    for key in lex:
        if lex[key] == value:
            x.append(key)
    return x  # Λίστα


def create_list(values, di):  # Χρησιμοποιεῖ τὴν return_keys
    q = []
    previous = None
    for value in values:
        keys = return_keys(di, value)
        if keys != previous:
            q.append([value, keys])
        previous = keys
    return q  # Λίστα (μὲ λίστα μέσα)


def sanitize(at, ex):
    for i in ex:
        at = at.replace(i, ' ')
    return at  # Συμβολοσειρά


exclude = {' ', '·', '–', '-', '"', '(', ')', '.', ',', '[', ']', ':'}  # Χαρακτήρες ποὺ θὰ ἀπαλειφθοῦν
for i in '0123456789':
    exclude.add(i)


# a = russel.russel_wiki_text()
a = lebowski.lebowski_text()
# a = genesis_old_testament.genesis_old_testament_text()


text = sanitize(a, exclude)  # συμβολοσειρά

text = text.replace('  ', ' ')
text = text.replace('  ', ' ')
text = text.replace('  ', ' ')


print(text)

d = letters_number(text)  # λεξικό: κλειδί=χαρακτῆρας, τιμή=πλῆθος ἐμφανίσεων
l = sorted(d.values(), reverse=True)  # πλήθη ἐμφανίσεων, φθίνουσα σειρά
q = create_list(l, d)  # q[i] = [πλῆθος, λίστα χαρακτήρων μὲ αὐτὸ τὸ πλῆθος]

words = text.split()  # λίστα

dw = letters_number(words)  # λεξικό: κλειδί=λέξη, τιμή=πλῆθος ἐμφανίσεων
lw = sorted(dw.values(), reverse=True)
qw = create_list(lw, dw)


print('\n')

print('Ἀριθμὸς χαρακτήρων:', len(text))
print('Ἀριθμὸς πραγματικῶν χαρακτήρων:', len(d))
print('\n')

for i in q:
    pct = i[0] / len(text) * 100
    print("%5d" % i[0], "%6.3f" % pct + '%', i[1])
print('\n')

print('Ἀριθμὸς λέξεων:', len(words))
print('Ἀριθμὸς πραγματικῶν λέξεων:', len(dw))
print('\n')
for i in qw:
    pct = i[0] / len(words) * 100
    print("%5d" % i[0], "%6.3f" % pct + '%', i[1][0:20])

print('\n')
