from problems.utils import mu, log


@log
def main():
    """
    https://projecteuler.net/problem=351
    http://mathworld.wolfram.com/TotientSummatoryFunction.html
    """
    N = 10 ** 8
    mu_values = mu(N)
    S = 0
    for i in range(1, N+1):
        k = N//i
        S += mu_values[i] * k * (1 + k)
    S //= 2
    return 6 * (N * (N + 1) // 2 - S)


if __name__ == '__main__':
    main()
