from problems.utils import log


@log
def main():
    """
    https://projecteuler.net/problem=16
    """
    return sum(map(int, str(2**1000)))


if __name__ == '__main__':
    main()
