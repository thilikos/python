# Παραδείγματα Python — Πληροφορική Ι

Μικρά προγράμματα για τη διδασκαλία της Python, οργανωμένα σε θεματικές ενότητες.
Ο κώδικας γράφτηκε αρχικά το 2017 και έχει εκσυγχρονιστεί ώστε να τρέχει σε
**Python 3.9+** με σύγχρονο ύφος (f-strings, `list.append`, εισαγωγές στην αρχή
του αρχείου, `if __name__ == "__main__"` όπου χρειάζεται).

## Ενότητες

| Φάκελος | Θέμα |
|---|---|
| `01_print input plot` | `print`, `input`, πρώτα γραφήματα με matplotlib |
| `02_for` | βρόχος `for` |
| `03_while` | βρόχος `while` |
| `04_while plus` | `while` — τυχαίοι περίπατοι, κόσκινο Ερατοσθένη |
| `05_functions` | συναρτήσεις, εμβέλεια μεταβλητών, ξεχωριστά modules |
| `06_morefunctions` | περισσότερες συναρτήσεις, animation, μεταθέσεις |
| `07_dictionaries` | λεξικά |
| `08_sets` | σύνολα, αναζήτηση, ταξινομήσεις |
| `09_strings` | συμβολοσειρές, ανάλυση κειμένου |
| `10_recursive` | αναδρομή, merge sort / bubble sort |

## Εκτέλεση

Χρειάζεται μόνο η `matplotlib` (για τα προγράμματα που κάνουν γραφήματα):

```bash
pip install -r requirements.txt
```

Μερικά προγράμματα εισάγουν βοηθητικά αρχεία από τον ίδιο φάκελο
(`import shuffle`, `import primes`, `import rwalk`, `import randoms`,
`import my_random_walk`, `import notes`). Τρέξ' τα από μέσα από τον φάκελό τους:

```bash
cd 08_sets
python3 selection.py
```

## Σημειώσεις

- Τα αρχεία στο `09_strings` (`russel.py`, `lebowski.py`, `kondylis.py`,
  `notes.py`, `genesis_old_testament.py`) είναι **δεδομένα** — μεγάλα κείμενα
  αποθηκευμένα ως συμβολοσειρά — και τα χρησιμοποιούν τα `all.py`,
  `text_analysis.py`, `make_notes.py`.
- Το `10_recursive/fibo.py` περιέχει αφελή αναδρομική Fibonacci· ο βρόχος
  επίδειξης φτάνει μέχρι το ~30 γιατί ο χρόνος μεγαλώνει εκθετικά.
- Οι εκδόσεις του 2017 διατηρούνται στο ιστορικό του git (κλάδος `main`,
  αρχική υποβολή).
