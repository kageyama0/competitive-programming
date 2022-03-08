import numpy as np
from itertools import combinations

n, m, x = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(n)]
# print(n, m, x, lis)

ans = 10 ** 9
for i in range(1, n+1):
    combination = combinations(range(n), i)
    for comb in combination:
        init = np.zeros(m+1)
        for ind in list(comb):
            init = init + np.array(lis[ind])
        if np.amin(init[1:]) >= x:
            print(init)
            ans = min(ans, init[0])
if ans < 10**9:
    print(int(ans))
else:
    print(-1)
