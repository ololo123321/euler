from utils import sieve_of_eratosthenes

if __name__ == '__main__':
    primes = sieve_of_eratosthenes(2000000)
    print(sum(primes))
