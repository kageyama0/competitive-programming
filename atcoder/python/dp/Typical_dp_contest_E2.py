mod = 10 ** 9 + 7
# d = int(input())
# n = inpupt()
d = 2
n = "15"

dp = [[0] * 2 for _ in range(d)]
dp[0][0] = 1

for x in map(int, n):
    ndp = [[0] * 2 for _ in range(d + 10)]
    for i in range(d):
        ndp[i][1] += dp[i][0]
        ndp[i + x][1] -= dp[i][0]
        ndp[i][1] += dp[i][1]
        ndp[i + 10][1] -= dp[i][1]
        print("x,i,ndp", x, i,ndp)


    acc = 0
    for i in range(d + 10):
        acc += ndp[i][1]
        ndp[i][1] = acc

    for i in range(d, d + 10):
        ndp[i % d][1] += ndp[i][1]

    for i in range(d):
        ndp[i][1] %= mod
        ndp[(i + x) % d][0] = dp[i][0]

    dp = ndp
    print(dp)

ans = (dp[0][0] + dp[0][1] - 1) % mod
print(ans)
