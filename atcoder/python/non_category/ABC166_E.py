from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

cnt = 0
d = defaultdict(int)
# j - i = Ai + Aj --> i + Ai = j - Aj
for i in range(n):
    cnt += d[i - A[i]]
    d[i + A[i]] += 1

print(cnt)
#print(L, R)
