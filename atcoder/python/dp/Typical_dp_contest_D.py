# https://atcoder.jp/contests/tdpc/tasks/tdpc_dice
# 素因数の数を数えることで、倍数かどうかを判定する


n, d = map(int, input().split())

# dp[i][j][k][l]:i回サイコロをふったとき、積の素因数に2がj個、3がk個、5がl個存在する確率。
#                j,k,lは、dの素因数個以上は保持しない。

r = []
for i in (2, 3, 5):
    c = 0
    while(d % i == 0):
        d //= i
        c += 1
    r.append(c)
# print(f'r:{r}')
if d != 1:
    print(0)
    exit()

dp = [[[[0 for _ in range(r[2]+1)] for _ in range(r[1]+1)]
       for _ in range(r[0]+1)] for _ in range(n+1)]
dp[0][0][0][0] = 1
x2 = [0, 1, 0, 2, 0, 1]
x3 = [0, 0, 1, 0, 0, 1]
x5 = [0, 0, 0, 0, 1, 0]
for i in range(n):
    for j in range(r[0]+1):
        for k in range(r[1]+1):
            for l in range(r[2]+1):
                for s in range(6):
                    dp[i+1][min(j+x2[s], r[0])][min(k+x3[s], r[1])
                                                ][min(l+x5[s], r[2])] += dp[i][j][k][l]/6
print(dp[n][r[0]][r[1]][r[2]])
