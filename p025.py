def main():
    f1, f2 = 1, 1
    n = 2
    while len(str(f2)) != 1000:
        f1, f2 = f2, f1 + f2
        n += 1
    return n

if __name__ == '__main__':
    print(main())
