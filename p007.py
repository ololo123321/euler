from utils import is_prime


def main():
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
    print(main())
