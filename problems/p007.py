from problems.utils import is_prime, log


@log
def main():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
    limit = 10001
    n = 2
    i = 0
    while True:
        if is_prime(n):
            i += 1
        if i == limit:
            break
        if n == 2:
            n += 1
        else:
            n += 2
    return n


if __name__ == '__main__':
    main()
