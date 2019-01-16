from utils import sieve_of_eratosthenes


def main():
    """
    O(nloglogn) algorithm
    time: ~2min 30sec

    desc: https://projecteuler.net/overview=351
    """
    n = 10**8
    primes = sieve_of_eratosthenes(n)
    tots = list(range(n+1))
    for p in primes:
        if p == tots[p]:
            k = p
            m = 1 - 1 / p
            while k <= n:
                tots[k] *= m
                k += p
    return int(sum(tots))

if __name__ == '__main__':
    print(main())
