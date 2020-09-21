from problems.utils import factorization, log


@log
def main():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    res = {}
    numbers = range(2, 21)
    for n in numbers:
        d = factorization(n)
        for k, v in d.items():
            res[k] = max(v, res.get(k, 0))
    m = 1
    for k, v in res.items():
        m *= k ** v
    return m


if __name__ == '__main__':
    main()
