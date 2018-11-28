from utils import divisors, gcd


def main(s):
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
    return triples


if __name__ == '__main__':
    a, b, c = main(1000)[0]
    print(a*b*c)
