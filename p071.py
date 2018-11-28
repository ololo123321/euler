"""
https://math.stackexchange.com/questions/39582/how-to-compute-next-previous-representable-rational-number
https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
"""
from utils import modinv


def main():
    p, q = 3, 7
    n = 1000000
    r = modinv(p, q)
    b = n
    while b % q != r:
        b -= 1
    return (b * p + 1) // q  # if p1/q1 < p2/p2, then q1*p2 - q2*p1 = 1

if __name__ == '__main__':
    print(main())
