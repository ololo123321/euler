def main():
    s = 0
    for n in range(1, 1000):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    return s

if __name__ == '__main__':
    print(main())
