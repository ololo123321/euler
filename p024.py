from math import factorial
from utils import log


@log
def main():
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
    of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
    we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    n = 10
    i = 1000000
    digits = list(range(n))
    res = digits.copy()
    j = 0
    k = 0
    while digits:
        p = factorial(n-k-1)
        if p < i:
            j += 1
            i -= p
        else:
            res[k] = digits.pop(j)
            k += 1
            j = 0
    return ''.join(map(str, res))


if __name__ == '__main__':
    main()
