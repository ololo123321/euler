from utils import log


@log
def main():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    n = 600851475143
    p = 2
    while n != 1 and p <= int(n ** 0.5):
        if n % p == 0:
            while n % p == 0:
                n /= p
            p = 1
        if p == 2:
            p += 1
        else:
            p += 2
    return max(int(n), p)


if __name__ == '__main__':
    main()
