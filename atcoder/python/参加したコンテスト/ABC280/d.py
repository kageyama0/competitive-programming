# 組み合わせの問題は、DPで計算省略できるかもと思おう...
n, K, d = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j][k]: 配列Aのi番目までで、j個の要素を選んで、その和の余りがkになる和の最大値
dp = [[[-1] * (d+1) for _ in range(K+1)] for _ in range(n+1)]

# 初期値
dp[0][0][0] = 0

for i in range(n):
    for j in range(K):
        for k in range(d):
            if dp[i][j][k] == -1:
                continue

            # 選ばない場合
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

            # 選ぶ場合
            if j != K:
                dp[i+1][j+1][(k+A[i]) % d] = \
                    max(dp[i+1][j+1][(k+A[i]) % d], dp[i][j][k] + A[i])

    # print(i, dp[i])

# print(*dp, sep="\n")
print(dp[n][K][0])
