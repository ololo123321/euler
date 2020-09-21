"""
https://math.stackexchange.com/questions/39582/how-to-compute-next-previous-representable-rational-number
https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
"""
from problems.utils import modinv, log


@log
def main():
    """
    Consider the fraction, n/d, where n and d are positive integers.
    If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that 2/5 is the fraction immediately to the left of 3/7.
    By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
    find the numerator of the fraction immediately to the left of 3/7.
    """
    p, q = 3, 7
    n = 1000000
    r = modinv(p, q)
    b = n
    while b % q != r:
        b -= 1
    return (b * p + 1) // q  # if p1/q1 < p2/p2, then q1*p2 - q2*p1 = 1


if __name__ == '__main__':
    main()
