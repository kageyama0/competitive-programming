# https://atcoder.jp/contests/abc035/tasks/abc035_c

# 参考: https://www.slideshare.net/chokudai/abc035

from itertools import accumulate

n, q = map(int, input().split())
imos = [0] * (n + 2)
for _ in range(q):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r+1] -= 1

ac = list(accumulate(imos))
print(*[ac[i] % 2 for i in range(1, n+1)], sep='')
