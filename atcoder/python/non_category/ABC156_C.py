n = int(input())
X = list(map(int, input().split()))
X.sort()
m = min(X)
M = max(X)

ans = float("inf")
for p in range(m, M + 1):
    cnt = 0
    for i in range(n):
        cnt += (X[i] - p) ** 2

    ans = min(ans, cnt)
print(ans)
