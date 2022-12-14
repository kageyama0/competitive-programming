def main():
    n = int(input())
    P = list(map(int, input().split()))
    m = float('inf')
    cnt = 0
    for i in range(n):
        if P[i] < m:
            cnt += 1
            m = P[i]
    print(cnt)


if __name__ == "__main__":
    main()
