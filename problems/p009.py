from problems.utils import divisors, gcd, log


@log
def main(s):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a2 + b2 = c2

    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    triples = []
    if s % 2 != 0:
        return triples
    s = int(s / 2)
    divisors_s = divisors(s)
    divisors_s.remove(1)
    for m in divisors_s:
        if m >= s ** 0.5:
            continue
        q = int(s / m)
        divisors_q = divisors(q)
        divisors_q.remove(1)
        for k in divisors_q:
            if m < k < 2*m and gcd(m, k) == 1:
                n = k - m
                d = int(q / k)
                a = (m ** 2 - n ** 2) * d
                b = 2 * m * n * d
                c = (m ** 2 + n ** 2) * d
                triples.append((a, b, c))
    a, b, c = triples[0]
    ans = a * b * c
    return ans


if __name__ == '__main__':
    main(s=1000)
