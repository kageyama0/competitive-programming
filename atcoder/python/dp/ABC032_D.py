# https://atcoder.jp/contests/abc032/tasks/abc032_d
# ナップザック問題
# TODO: なんか動かない。入力値が大きすぎる？

N, W = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1,N+1):
    v, w = map(int, input().split())
    for j in range(W + 1):
        # i番目の品物を選べる場合
        if j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

        # i番目の品物を選べない場合
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

# print(*dp, sep="\n")
print(dp[-1][-1])
