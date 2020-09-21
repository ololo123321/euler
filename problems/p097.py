from problems.utils import log


@log
def main():
    """
    https://projecteuler.net/problem=97
    """
    m = 28433
    p = 7830457
    q = 10 ** 10
    mod = 1
    for _ in range(p):
        mod = (mod * 2) % q
    return (m * mod + 1) % q


if __name__ == '__main__':
    main()
