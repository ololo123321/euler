from problems.utils import gcd, log


def all_pairs_from_primitive(a, b, M):
    res = [(a, b)]
    k = 2
    while True:
        a_ = a * k
        b_ = b * k
        if (a_ <= 2*M and b_ <= M) or (b_ <= 2*M and a_ <= M):
            res.append((a_, b_))
            k += 1
        else:
            break
    return res


def all_pairs(M):
    """
    получить все пары (a,b) такие, что:
    1. a <= 2M, b <= M или b <= 2M, a <= M
    2. a = m ** 2 - n ** 2
    3. b = 2 * m * n
    4. m > n
    5. m и n имеют разную чётность
    6. gcd(m, n) == 1
    """
    m = 2
    n = 1
    res = []
    while True:
        a = m ** 2 - n ** 2
        b = 2 * m * n
        if (a <= 2*M and b <= M) or (b <= 2*M and a <= M):
            res += all_pairs_from_primitive(a, b, M)
            m += 2 
            while gcd(m, n) != 1:
                m += 2
        elif m - n == 1:
            break
        else:
            n += 1
            m = n + 1
    return res


def all_combinations(a, bc, M):
    if 2*a < bc:  # a не самая длинная сторона
        return 0
    if a > M:  # очевидно
        return 0
    if a >= bc:  # а длиннее суммы двух других сторон
        return bc // 2
    return a - (bc - 1) // 2  # bc - (bc - a) - (bc - 1) // 2, геометрически это удобно показать
                              # bc - 1 - чтоб при чётном bc учитывалась пара (bc / 2, bc / 2)


def cuboids_number(M):
    pairs = all_pairs(M)
    N = 0
    for a, b in pairs:
        N += all_combinations(a, b, M)
        N += all_combinations(b, a, M)
    return N


@log
def main():
    """
    https://projecteuler.net/problem=86
    """
    N = 1e6
    M = 1
    while cuboids_number(M) <= N:
        M += 1
    return M


if __name__ == '__main__':
    main()
