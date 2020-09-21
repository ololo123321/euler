from math import factorial
from problems.utils import log


def f(n, k):
    res = 1
    for i in range(n, n-k, -1):
        res *= i
    return res // factorial(k)


@log
def main():
    """
    https://projecteuler.net/problem=53
    """
    S = 0
    limit = 1000000
    for n in range(1, 101):
        for k in range(n+1):
            if f(n, k) > limit:
                S += n-(k-1)*2-1
                break
    return S


if __name__ == '__main__':
    main()
