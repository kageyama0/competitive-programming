N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
else:
    right, ans, tmp = 0, 0, 1
    for left in range(N):
        # print("left:", left, "right:", right, "ans:", ans, "tmp:", tmp)

        # 右端に到達するまで、かつ、右端に到達するまでの積がK以下の間
        while right < N and tmp*S[right] <= K:
            tmp *= S[right]
            right += 1
        ans = max(ans, right-left)

        # 1つだけでKを超えてしまっていた場合、+1
        if left == right:
            right += 1
        # それまでの積からS[left]を割ることで、左端を+1した場合の積を求める。
        else:
            tmp //= S[left]
    print(ans)
