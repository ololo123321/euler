from utils import factorization


def phi(n):
    """
    https://en.wikipedia.org/wiki/Euler's_totient_function
    """
    if n % 2 == 0:
        n //= 2
        if n % 2 == 0:
            return 2*phi(n)
        return phi(n)
    d = factorization(n)
    ans = n
    for p in d:
        ans *= 1 - 1 / p
    return int(ans)


def main():
    ans = 2
    value = 0
    for n in range(2, 1000001):
        m = phi(n)
        v = n / m
        if v > value:
            ans = n
            value = v
    return ans

if __name__ == '__main__':
    print(main())
