import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
# IN = lambda:map(int, input().split())
# n,k = IN()
n, k = map(int, readline().split())
dp = np.zeros(k + 1)

for i in range(n):
    w, c = map(int, readline().split())
    print(dp[w:], dp[:-w])
    dp[w:] = np.maximum(dp[w:], dp[:-w] + c)
print(dp)
print(int(dp[-1]))
