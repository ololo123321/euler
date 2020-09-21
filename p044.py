from utils import log


def pentagonal_numbers_generator():
    n = 1
    while True:
        yield int((3*n**2 - n) / 2)
        n += 1


def is_pentagonal(n):
    q = (1 + (1 + 24*n) ** 0.5) / 6
    if q.is_integer():
        return True
    return False


@log
def main():
    """
    https://projecteuler.net/problem=44
    """
    gen = pentagonal_numbers_generator()
    s = set()
    while True:
        pi = next(gen)
        for pj in s:
            if is_pentagonal(pi-pj) and is_pentagonal(pi+pj):
                return pi-pj
        s.add(pi)


if __name__ == '__main__':
    main()
