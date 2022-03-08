N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [0] + [None] * (N - 1)
for i in range(1, N):
    dp[i] = min(dp[j] + abs(h[i] - h[j]) for j in range(max(i - K, 0), i))

print(dp[-1])
