"""
http://www.geocities.ws/fredlb37/triples10.pdf
"""
from collections import defaultdict
from itertools import combinations
from utils import gcd, log


def get_all_triples(M):
    m = 2
    n = 1
    res = []
    while True:
        a = m ** 2 - n ** 2
        b = 2 * m * n + n ** 2
        c = m ** 2 + n ** 2 + m * n
        if a + b < M:
            res.append((a, b, c))
            k = 2
            while True:
                a_ = a * k
                b_ = b * k
                c_ = c * k
                if a_ + b_ < M:
                    res.append((a_, b_, c_))
                    k += 1
                else:
                    break
            m += 1
            while gcd(m, n) != 1 or (m - n) % 3 == 0:
                m += 1
        elif m - n == 1:
            break
        else:
            n += 1
            m = n + 1
    return res


@log
def main():
    """
    https://projecteuler.net/problem=143
    """
    M = 120000
    all_triples = get_all_triples(M)

    d = defaultdict(list)
    for t in all_triples:
        d[min(t[:2])].append(t)
        d[max(t[:2])].append(t)

    res = set()

    for p, triples in d.items():
        for t1, t2 in combinations(triples, 2):
            q = t1[0] if t1[0] != p else t1[1]
            r = t2[0] if t2[0] != p else t2[1]
            a = (q ** 2 + r ** 2 + q * r) ** 0.5
            s = p + q + r
            if a.is_integer() and s <= M:
                res.add(s)

    return sum(res)


if __name__ == '__main__':
    main()
