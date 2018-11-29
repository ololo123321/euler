import numpy as np
from utils import sieve_of_eratosthenes


def main():
    N = 10 ** 8
    primes = sieve_of_eratosthenes(N)
    # https://en.wikipedia.org/wiki/M%C3%B6bius_function
    mu = np.ones(N+1, dtype='int')
    for p in primes:
        mu[::p] *= -1
        mu[::p**2] = 0

    # http://mathworld.wolfram.com/TotientSummatoryFunction.html
    S = 0
    for i in range(1, N+1):
        k = N//i
        S += mu[i] * k * (1 + k)
    S //= 2
    return 6 * (N * (N + 1) // 2 - S)

if __name__ == '__main__':
    print(main())
