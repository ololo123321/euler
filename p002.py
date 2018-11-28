def main():
    s = 0
    f0, f1 = 1, 2
    while f1 < 4e6:
        if f1 % 2 == 0:
            s += f1
        f0, f1 = f1, f0 + f1
    return s

if __name__ == '__main__':
    print(main())
