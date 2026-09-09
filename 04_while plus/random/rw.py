import random


def random_walk(n):
    x = 0
    y = 0
    steps = 0
    # Ο τυχαίος περίπατος:
    while abs(x) < n and abs(y) < n:  # όσο δεν έχει φτάσει στην άκρη
        r = random.random()
        if r < 0.25:
            y += 1   # Πήγαινε επάνω
        elif r < 0.5:
            x += 1   # Πήγαινε δεξιά
        elif r < 0.75:
            y -= 1   # Πήγαινε κάτω
        else:
            x -= 1   # Πήγαινε αριστερά
        steps += 1
    return steps


def main():
    n_trials = 10000  # πλήθος δοκιμών για κάθε μέγεθος τετραγώνου
    print('Aποτελέσματα βασισμένα σε', n_trials, 'δοκιμές.')
    print('Μέγεθος Μ.Ο. βημάτων')
    for n in range(5, 51, 5):  # για διάφορα μεγέθη τετραγώνων
        steps = 0
        for k in range(n_trials):
            steps += random_walk(n)
        avg = steps / n_trials
        print(n, '\t', format(avg, '9.3f'))


if __name__ == '__main__':
    main()
