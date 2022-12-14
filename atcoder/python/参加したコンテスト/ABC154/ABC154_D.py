import numpy as np

n, k = map(int, input().split())
P = np.array([0] + list(map(int, input().split())))
C = np.cumsum(P)
print(C)
M = 0
for i in range(n - k):
    print(C[i + k + 1], C[i])
    M = max(M, C[i + k + 1] - C[i])

ans = (M + k) / 2
print(ans)
