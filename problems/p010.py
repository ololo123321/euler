from problems.utils import sieve_of_eratosthenes, log


@log
def main():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    n = 2000000
    primes = sieve_of_eratosthenes(n)
    ans = sum(primes)
    return ans


if __name__ == '__main__':
    main()
