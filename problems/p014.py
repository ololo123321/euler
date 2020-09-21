from problems.utils import log


@log
def main():
    """
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    limit = 1000000
    d = {1: 1}
    for s in range(2, limit+1):
        if s % 2 == 0:
            d[s] = d[s / 2] + 1
            continue
        k = s * 3 + 1
        n = 1
        while k > s - 1:
            if k % 2 == 0:
                k /= 2
            else:
                k = k * 3 + 1
            n += 1
        d[s] = d[k] + n
    ans = max(d, key=d.get)
    return ans


if __name__ == '__main__':
    main()
