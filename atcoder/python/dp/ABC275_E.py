# ルーレットも結局組み合わせの問題なので、DPか
# modの逆数
# https://kyo-pro.hatenablog.com/entry/Modular-multiplicative-inverse

MOD = 998244353
n, m, k = map(int, input().split())

# dp[i][j]: i回ルーレットを回して、現在地がjのとき確率
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1
# mのmod上での逆数
m_inv = pow(m, MOD - 2, MOD)

# i回目のルーレットを回し、現在地がj(0 ~ n-1)の時に、ルーレットでx(1 ~ m)が出る確率
for i in range(1, k+1):
    for j in range(n):
        for x in range(1, m+1):
            next_j = j + x if j + x <= n else 2 * n - j - x
            dp[i][next_j] += dp[i-1][j] * m_inv % MOD
            dp[i][next_j] %= MOD

# print(*dp, sep="\n")
# print(dp[k][n])

ans = 0
for dp_i in dp:
    ans += dp_i[n]
    ans %= MOD

print(ans)
