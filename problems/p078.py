from problems.utils import log


def multiplier(x):
    return 1 if x % 4 == 1 or x % 4 == 2 else -1


def generalized_pentagonal_numbers_generator():
    k = 1
    while True:
        if k < 0:
            k = abs(k) + 1
        else:
            k *= -1
        yield int((3*k**2 - k) / 2)


@log
def main():
    """
    https://projecteuler.net/problem=78
    """
    numbers = [1]
    gen = generalized_pentagonal_numbers_generator()
    m_next = next(gen)
    d = {0: 1}
    n = 1
    while True:
        if n == m_next:
            numbers.append(n)
            m_next = next(gen)
        coefs = [n - i for i in numbers]
        q = sum(multiplier(i) * d[j] for i, j in enumerate(coefs, 1))
        d[n] = q
        if q % 1000000 == 0:
            return n
        n += 1


if __name__ == '__main__':
    main()
