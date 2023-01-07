# https://atcoder.jp/contests/abc014/tasks/abc014_3

from itertools import accumulate
n = int(input())

imos = [0] * (10 ** 6 + 2)
for _ in range(n):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b + 1] -= 1

ac = list(accumulate(imos))
print(max(ac))
