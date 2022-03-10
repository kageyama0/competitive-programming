# https://atcoder.jp/contests/tdpc/submissions/2559581
from itertools import accumulate
na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.reverse()
b.reverse()

sa = [0] + list(accumulate(a))
sb = [0] + list(accumulate(b))

dp = [[0 for j in range(nb + 1)] for i in range(na + 1)]

# Aの山の下からi個,Bの山の下からj個とったときのすね毛くんのスコア
for i in range(na + 1):
    for j in range(nb + 1):
        if i == 0 and j == 0:
            dp[i][j] = 0

        elif i == 0:
            dp[i][j] = sb[j] - dp[i][j - 1]

        elif j == 0:
            dp[i][j] = sa[j] - dp[i - 1][j]

        else:
            dp[i][j] = sa[i] + sb[j] - min(dp[i - 1][j], dp[i][j - 1])

        print(i, j, dp[i][j])

print(dp[na][nb])
