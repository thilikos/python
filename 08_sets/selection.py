import shuffle

# Ταξινόμηση μὲ ἐπιλογὴ (selection sort), τυπώνοντας κάθε βῆμα


def selection(v):
    for i in range(len(v) - 1):
        min_index = i
        for j in range(i + 1, len(v)):
            if v[j] < v[min_index]:
                min_index = j
        if min_index != i:
            v[i], v[min_index] = v[min_index], v[i]
        print(v)
    return v


v = shuffle.create(20, 20)

print(v)
print(selection(v))
