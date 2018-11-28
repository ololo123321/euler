from utils import factorization


def main():
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
    print(main())
