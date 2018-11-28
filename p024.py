from math import factorial


def main():
    n = 10
    i = 1000000
    digits = list(range(n))
    res = digits.copy()
    j = 0
    k = 0
    while digits:
        p = factorial(n-k-1)
        if p < i:
            j += 1
            i -= p
        else:
            res[k] = digits.pop(j)
            k += 1
            j = 0
    return ''.join(map(str, res))

if __name__ == '__main__':
    print(main())
