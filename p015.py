from scipy.special import comb
from utils import log


@log
def main():
    """
    https://projecteuler.net/problem=15
    """
    n = 20
    return comb(n*2, n, exact=True)


if __name__ == '__main__':
    main()
