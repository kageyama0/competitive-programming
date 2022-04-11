# https://atcoder.jp/contests/tdpc/submissions/2559581
from itertools import accumulate
na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.reverse()
b.reverse()

sa = [0] + list(accumulate(a))
sb = [0] + list(accumulate(b))
# print(sa,sb)

dp = [[0 for j in range(nb + 1)] for i in range(na + 1)]

# dp[i][j]: Aがあとi個、Bがあとj個残っている状態から始めた時のスコア
for i in range(na + 1):
    for j in range(nb + 1):
        if i == 0 and j == 0:
            dp[i][j] = 0

        # Aから選んでいないとき。Aから選んでいないので、Aの累積和は考えなくて良い
        elif i == 0:
            dp[i][j] = sb[j] - dp[i][j - 1]

        # Bから選んでいないとき。Bから選んでいないので、Bの累積和は考えなくて良い
        elif j == 0:
            dp[i][j] = sa[i] - dp[i - 1][j]

        # dp[i-1][j]とdp[i][j-1]のどちらかから遷移してくる
        else:
            dp[i][j] = sa[i] + sb[j] - min(dp[i - 1][j], dp[i][j - 1])

# print(*dp, sep='\n')
print(dp[na][nb])
