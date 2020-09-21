from itertools import permutations
from operator import add, sub, truediv, mul
from problems.utils import log


def traverse(numbers):
    nodes = [numbers]
    res = set()
    for node in nodes:
        for a, b in permutations(node, 2):
            for op in [add, sub, truediv, mul]:
                if a > b and op.__name__ in ['add', 'mul']:
                    continue

                if b == 0 and op.__name__ == 'truediv':
                    continue
                else:
                    c = op(a, b)

                child = node.copy()
                child.remove(a)
                child.remove(b)
                if child:
                    child.append(c)
                    nodes.append(child)
                else:
                    if float(c).is_integer() and c > 0:
                        res.add(int(c))
    return sorted(res)


def seq_len(numbers):
    if numbers[0] != 1:
        return 0
    k = 0
    n0 = numbers[0]
    for n1 in numbers[1:]:
        if n1-n0 == 1:
            k += 1
            n0 = n1
        else:
            break
    return k+1


@log
def main():
    """
    By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the
    four arithmetic operations (+, −, *, /) and brackets/parentheses,
    it is possible to form different positive integer targets.

    For example,

    8 = (4 * (1 + 3)) / 2
    14 = 4 * (3 + 1 / 2)
    19 = 4 * (2 + 3) − 1
    36 = 3 * 4 * (2 + 1)

    Note that concatenations of the digits, like 12 + 34, are not allowed.

    Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is
    the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
    Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers,
    1 to n, can be obtained, giving your answer as a string: abcd.
    """
    l_max = 0
    best_numbers = None
    for i in range(1, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for m in range(k + 1, 10):
                    numbers = [i, j, k, m]
                    res = traverse(numbers)
                    l = seq_len(res)
                    if l > l_max:
                        l_max = l
                        best_numbers = numbers
    return ''.join(map(str, best_numbers))


if __name__ == '__main__':
    main()
