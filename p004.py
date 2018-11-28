def is_palindrome(n):
    if 10 ** 4 <= n < 10 ** 5 and n // 10000 == n % 10 and (n % 10 ** 4 - n % 10 ** 3) / 10 ** 3 == (
            n % 10 ** 2 - n % 10) / 10:
        return True
    elif 10 ** 5 <= n < 10 ** 6 and n // 10 ** 5 == n % 10 and (n % 10 ** 5 - n % 10 ** 4) / 10 ** 4 == (
            n % 10 ** 2 - n % 10) / 10 and (n % 10 ** 4 - n % 10 ** 3) / 10 ** 3 == (
            n % 10 ** 3 - n % 10 ** 2) / 10 ** 2:
        return True
    return False


def main():
    p_max = 10000
    for i in range(100, 1000):
        for j in range(100, 1000):
            p = i * j
            if is_palindrome(p):
                if p > p_max:
                    p_max = p
    return p_max


if __name__ == '__main__':
    print(main())
