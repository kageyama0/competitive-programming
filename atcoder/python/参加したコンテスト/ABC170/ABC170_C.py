def main():
    x, n = map(int, input().split())
    P = list(map(int, input().split()))
    m = x
    M = x
    if len(P) == 0:
        print(x)
        exit()
    if not x in P:
        print(x)
        exit()

    while True:
        m -= 1
        M += 1
        if not m in P:
            print(m)
            exit()
        if not M in P:
            print(M)
            exit()



if __name__ == "__main__":
    main()
