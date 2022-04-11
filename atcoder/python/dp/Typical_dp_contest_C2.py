# https://atcoder.jp/contests/tdpc/tasks/tdpc_tournament
# トーナメント

K = int(input())

# N人で行うコンテスト
N = 1 << K
# 各人のレート
A = [int(input()) for _ in range(N)]

dp = [[0] * N for _ in range(K + 1)]

for i in range(N):
    dp[0][i] = 1


def calc(p, q):
    return 1/(1 + 10**((A[q] - A[p])/400))


# dp[i][j]: i回戦目でj番目の人が勝つ確率
# ただし、インデックスの関係上、普通の１回戦のことを0回戦目として、１番目の人は0番目の人としている。
# i回戦目の計算
for i in range(K):
    # L番目〜R番目までの人が対戦した時にそれぞれが勝つ確率を求める
    for L in range(0, N, 1 << (i + 1)):
        M = L + (1 << i)
        R = L + (1 << (i + 1))

        # i番目の人が、左側のトーナメントにいる場合
        for j in range(L, M):
            res = 0
            # 対戦相手がk番目の人になる場合
            for k in range(M, R):
                res += calc(j, k) * dp[i][k]
            dp[i + 1][j] = res * dp[i][j]

        # i番目の人が、右側のトーナメントにいる場合
        for j in range(M, R):
            res = 0
            # 対戦相手がk番目の人になる場合
            for k in range(L, M):
                res += calc(j, k) * dp[i][k]
            dp[i + 1][j] = res * dp[i][j]


for i in range(N):
    print(dp[K][i])
