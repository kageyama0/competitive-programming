# 解説通りに実装してみた場合

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(N):
    B.append((A[i], i))

B = sorted(B, key=lambda x: (x[0], -x[1]))

mx = -float("inf")
ans = float("inf")
for v, i in B:
    if i < K:
        mx = max(mx, i)
    else:
        ans = min(ans, i-mx)

if ans == float("inf"):
    print(-1)
else:
    print(ans)
