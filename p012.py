from utils import divisors_number


def main():
    i = 1
    n = i
    while True:
        q = divisors_number(n)
        if q > 500:
            return n
        i += 1
        n += i

if __name__ == '__main__':
    print(main())
