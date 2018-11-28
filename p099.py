from math import log


def main():
    n_max = 0
    i_max = 0
    with open('p099_base_exp.txt') as f:
        for i, r in enumerate(f.readlines(), 1):
            base, exp = map(int, r.strip().split(','))
            n = exp / log(2, base)
            if n > n_max:
                n_max = n
                i_max = i
    return i_max


if __name__ == '__main__':
    print(main())
