from utils import phi, log


@log
def main():
    """
    https://projecteuler.net/problem=69
    """
    ans = 2
    value = 0
    for n in range(2, 1000001):
        m = phi(n)
        v = n / m
        if v > value:
            ans = n
            value = v
    return ans


if __name__ == '__main__':
    main()
