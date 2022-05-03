N, P = map(int, input().split())

dp = [[0]*(N+2) for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    if i != 0:
        for j in range(N+1):
            dp[i][j+1] = (dp[i][j]+dp[i][j+1]) % P
    for j in range(N):
        plusl = dp[i][j]*26 if i == 0 else dp[i][j]*25
        l, k = 1, 2
        while j+l <= N and i+k <= N-1:
            r = min(l*10, N-j+1)
            dp[i+k][j+l] = (dp[i+k][j+l]+plusl) % P
            dp[i+k][j+r] = (dp[i+k][j+r]-plusl) % P
            l, k = l*10, k+1

# for i in dp:
#     print(i)
print(sum([dp[i][N] for i in range(N)]) % P)
