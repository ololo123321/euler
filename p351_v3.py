from utils import log


@log
def main():
    """
    O(n**(3/4)) algorithm
    time: ~2sec

    desc: https://projecteuler.net/overview=351
    """
    n = 10 ** 8
    isqrt_n = int(n ** 0.5)
    v = [0] * (isqrt_n + 1)
    V = [0] * (n // isqrt_n + 1)
    for x in range(1, isqrt_n + 1):
        res = x * (x + 1) // 2
        isqrt_x = int(x ** 0.5)

        for g in range(2, isqrt_x + 1):
            res -= v[x // g]

        for z in range(1, isqrt_x + 1):
            if z != x // z:
                res -= (x // z - x // (z + 1)) * v[z]
        v[x] = res

    for x in range(n // isqrt_n, 0, -1):
        k = n // x
        res = k * (k + 1) // 2
        isqrt_k = int(k ** 0.5)

        for g in range(2, isqrt_k + 1):
            if k // g <= isqrt_n:
                res -= v[k // g]
            else:
                res -= V[x * g]

        for z in range(1, isqrt_k + 1):
            if z != k // z:
                res -= (k // z - k // (z + 1)) * v[z]
        V[x] = res
    return V[1]


if __name__ == '__main__':
    main()
