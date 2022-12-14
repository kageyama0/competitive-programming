
N, M, K = map(int, input().split())
MOD = 998244353

# dp[i][j]: 先頭からi番目まで決めた時に総和がjである組み合わせの数
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(1, K+1):
        for k in range(1, M+1):
            # print(i,j,k)
            if j-k >= 0:
                dp[i+1][j] += dp[i][j-k]


ans = 0
for i in range(1, K+1):
    ans += dp[N][i] % MOD

print(ans % MOD)
