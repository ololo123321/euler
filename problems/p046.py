from problems.utils import is_prime, log


@log
def main():
    """
    https://projecteuler.net/problem=46
    """
    primes = [2]
    n = 1
    while True:
        n += 2
        if is_prime(n):
            primes.append(n)
            continue
        is_bad = True
        for p in primes:
            q = ((n - p) / 2) ** 0.5
            if q.is_integer():
                is_bad = False
                break
        if is_bad:
            return n


if __name__ == '__main__':
    main()
