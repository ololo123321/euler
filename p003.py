def main():
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
    print(main())
