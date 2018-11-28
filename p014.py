def main():
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
    return max(d, key=d.get)


if __name__ == '__main__':
    print(main())
