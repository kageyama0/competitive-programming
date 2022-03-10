N = int(input())
h = list(map(int, input().split()))
dp = [0] * N
dp[1] = abs(h[1] - h[0])
for i in range(N - 2):
    dp[i + 2] = min(dp[i + 1] + abs(h[i + 2] - h[i + 1]),
                    dp[i] + abs(h[i + 2] - h[i]))

print(dp[-1])
