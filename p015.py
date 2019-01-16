from scipy.special import comb


def main():
    n = 20
    return comb(n*2, n, exact=True)

if __name__ == '__main__':
    print(main())
