def main():
    x, n = map(int, input().split())
    P = list(map(int, input().split()))
    m = x
    M = x
    if len(P) == 0:
        print(x)
        exit()
    if x not in P:
        print(x)
        exit()

    while True:
        m -= 1
        M += 1
        if m not in P:
            print(m)
            exit()
        if M not in P:
            print(M)
            exit()


if __name__ == "__main__":
    main()
