from numpy.polynomial.polynomial import polypow


def get_probs(n_dice, n_turns):
    p = [1 / n_dice] * n_dice
    return polypow(p, n_turns)


def main():
    probs4 = get_probs(4, 9)
    probs6 = get_probs(6, 6)
    res = 0
    for i, p in enumerate(probs4, 9):
        res += p * probs6[:i - 6].sum()
    return round(res, 7)

if __name__ == '__main__':
    print(main())
