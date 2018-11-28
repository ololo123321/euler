def main():
    s0 = 0
    s1 = 0
    for i in range(1, 101):
        s0 += i**2
        s1 += i
    return s1**2 - s0


if __name__ == '__main__':
    print(main())
