def main():
    n = 12000
    i = 0
    flag = False
    a, b, c, d = 0, 1, 1, n
    while True:
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        if a == 1 and b == 3:
            flag = True
        if flag:
            i += 1
        if c == 1 and d == 2:
            return i-1

if __name__ == '__main__':
    print(main())
