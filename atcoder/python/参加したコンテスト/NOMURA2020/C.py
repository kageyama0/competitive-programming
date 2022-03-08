def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * (n+1)
    if n == 0:
        x = A[0]
        if x == 1:
            print(1)
        else:
            print(-1)
        exit()
    # Adが葉の個数、Bdが葉でないものの個数
    # A0 + B0 = 1
    # Bd ≤ Ad+1 + Bd+1 ≤ 2Bd --> B[d-1] - A[d] ≤ B[d] ≤ 2B[d-1] - A[d]
    # Bd ≤ Ad+1 + Ad+2 + · · · + AN = s - (A1 + ... + Ad)

    # now_s :葉の数
    now_s = sum(A)
    s = now_s
    for i in range(n+1):
        if i == 0:
            B[i] = 1 - A[i]
        else:
            now_s -= A[i]
            B[i] = min(now_s, 2 * B[i - 1] - A[i])
            #print(A,B,now_s)
            if B[i] < 0:
                print(-1)
                exit()

    print(sum(B) + s)


if __name__ == "__main__":
    main()
