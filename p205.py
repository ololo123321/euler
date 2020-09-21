from numpy.polynomial.polynomial import polypow
from utils import log


def get_probs(n_dice, n_turns):
    p = [1 / n_dice] * n_dice
    return polypow(p, n_turns)


@log
def main():
    """
    Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
    Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

    Peter and Colin roll their dice and compare totals: the highest total wins.
    The result is a draw if the totals are equal.
    What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places
    in the form 0.abcdefg
    """
    probs4 = get_probs(4, 9)
    probs6 = get_probs(6, 6)
    res = 0
    for i, p in enumerate(probs4, 9):
        res += p * probs6[:i - 6].sum()
    return round(res, 7)


if __name__ == '__main__':
    main()
