from problems.utils import log


def coins_sum(n, coins):
    table = [1] + [0] * n
    for c in coins:
        for j in range(c, n+1):
            table[j] += table[j-c]
    return table[-1]


@log
def main():
    """
    https://projecteuler.net/problem=31
    """
    n = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    return coins_sum(n, coins)


if __name__ == '__main__':
    main()
