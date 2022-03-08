import numpy as np
n, k = map(int, input().split())
c = [0] * (10**5+1)
for _ in range(n):
  a, b = map(int, input().split())
  c[a] += b

A = np.array(c, dtype=np.int32)
A = A.cumsum()
answer = (A >= k).nonzero()[0].min()
print(answer)
