from itertools import product
from math import factorial


def gcd(a, b):
    q = a // b
    r = a - b*q
    if r:
        return gcd(b, r)
    return b


def is_prime(n):
    """
    1. Все простые числа кроме 2 и 3 представимы в виде 6k +- 1
    2. Если n не делится ни на одно из чисел p <= n**0.5, то n - простое
    """
    if n < 5:
        if n == 2 or n == 3:
            return True
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    p = 5
    while p <= n ** 0.5:
        if n % p == 0 or n % (p+2) == 0:
            return False
        p += 6
    return True


def factorization(n):
    d = {}
    k = 2
    while True:
        if n % k == 0:
            d[k] = 0
            while n % k == 0:
                n //= k
                d[k] += 1
        elif k > n ** 0.5:
            if n != 1:
                d[n] = 1
            break
        if k == 2:
            k += 1
        else:
            k += 2
    return d


def divisors(n):
    if n == 1:
        return [1]
    d = factorization(n)
    prime_factors = d.keys()
    res = []
    for powers in product(*[range(v+1) for v in d.values()]):
        div = 1
        for i, j in zip(prime_factors, powers):
            div *= i**j
        res.append(div)
    return res


def divisors_number(n):
    if n == 1:
        return 1
    d = factorization(n)
    m = 1
    for v in d.values():
        m *= v+1
    return m


def combination(n, k):
    return int(factorial(n) / factorial(k) / factorial(n - k))


def sieve_of_eratosthenes(n):
    mask = [False] * 2 + [True] * (n - 1)
    i = 2
    while i <= n ** 0.5:
        if mask[i]:
            j = i**2
            while j <= n:
                mask[j] = False
                j += i
        i += 1
    return [i for i, a in enumerate(mask) if a]


def egcd(a, b):
    """
    finds g,x,y such that ax + by = g, where g = gcd(a,b)
    """
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m
