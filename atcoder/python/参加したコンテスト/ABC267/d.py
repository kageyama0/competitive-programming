# どれ選ぶかみたいな組み合わせの問題はDPですやん
# 全部マイナスの値の場合があるので、単純ではないけど
n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

# dp[i][j]: i番目までの数字を使って、j個の数字を使った場合の部分列の最大値
# 負の数しかなくて選ばざるを得ない時があるので、初期値を-10**9にしておく
INF = float("inf")
dp = [[-INF] * (m+1) for _ in range(n+1)]
dp[0][0] = 0


for i in range(1, n+1):
    for j in range(m+1):
        # 0個選ぶ場合は、何も選ばないので、0にしておく
        if j == 0:
            dp[i][j] = 0
            continue

        # i番目において、選べる数はi個までであり、j個より大きい数を使えないので、スキップ
        if i < j:
            continue

        # print(f"i:{i}, j:{j}")
        # print(f"dp[i][j]:{dp[i][j]}, dp[i-1][j-1]:{dp[i-1][j-1]}, j * A[i]:{j * A[i]}")
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + j * A[i])

print(dp[-1][-1])
