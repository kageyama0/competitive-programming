# https://atcoder.jp/contests/dp/tasks/dp_d
# 参考：https://qiita.com/drken/items/dc53c683d6de8aeacf5a#d-%E5%95%8F%E9%A1%8C---knapsack-1
# ナップサック問題

N, W = map(int, input().split())
# wv = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]:i個目までの品物から選んだときに、重さがj以下になるように選んだ品物の総重量
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(1,N+1):
    w, v = map(int, input().split())
    for j in range(W+1):
        # i番目の品物を選ぶ場合
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

        # i番目の品物を選ばない場合
        dp[i][j] = max(dp[i][j], dp[i-1][j])

# print(*dp, sep='\n')
print(dp[-1][-1])
