from itertools import product
from datetime import datetime
import numpy as np


def log(func):
    def logged(*args, **kwargs):
        print(f"{func.__name__} started.")
        t0 = datetime.now()
        res = func(*args, **kwargs)
        time_elapsed = datetime.now() - t0
        print(f"{func.__name__} finished. Time elapsed: {time_elapsed}")
        print(f"answer: {res}")
    return logged


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
    if n % 2 == 0:
        d[2] = 0
        while n % 2 == 0:
            n //= 2
            d[2] += 1
    k = 3
    while k <= n:
        if n % k == 0:
            d[k] = 0
            while n % k == 0:
                n //= k
                d[k] += 1
        k += 2
    if n != 1:
        d[n] = 1
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


def phi(n):
    """
    https://en.wikipedia.org/wiki/Euler's_totient_function
    """
    d = factorization(n)
    ans = n
    for p in d:
        ans *= 1 - 1 / p
    return int(ans)


def mu(n):
    """
    Значения функции Мёбиуса для всех натуральных чисел от 1 до n
    https://en.wikipedia.org/wiki/M%C3%B6bius_function
    """
    primes = sieve_of_eratosthenes(n)
    res = np.ones(n+1, dtype='int8')
    for p in primes:
        res[::p] *= -1
        res[::p**2] = 0
    return res


def linear_sieve(n):
    if n == 1:
        return 0
    lp = [0] * (n+1)
    pr = []
    for i in range(2, n+1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        for p in pr:
            k = i * p  # проход по числам, кратным i
            if p <= lp[i] and k <= n:
                lp[k] = p
    return pr, lp


def factorization_from_least_primes(n, lp):
    """
    Факторизация числа n с помощью массива
    наименьших простых делителей чисел от 1 до n
    """
    d = {}
    while n != 1:
        k = lp[n]
        d[k] = 0
        while n % k == 0:
            n //= k
            d[k] += 1
    return d
