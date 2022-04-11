# https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3] * n
dp[0][0], dp[0][1], dp[0][2] = abc[0][0], abc[0][1], abc[0][2]
for i in range(n-1):
    dp[i + 1][0], dp[i + 1][1], dp[i + 1][2] = (abc[i + 1][0] + max(dp[i][1], dp[i][2]),
                                                abc[i + 1][1] +
                                                max(dp[i][2], dp[i][0]),
                                                abc[i + 1][2] + max(dp[i][0], dp[i][1]))
print(max(dp[-1]))
