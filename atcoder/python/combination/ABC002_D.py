# https://atcoder.jp/contests/abc002/tasks/abc002_4
n, m = map(int, input().split())
# list ではなく、set(tuple())をつかっている。後の12行目の表現をするためか？
s = set(tuple(map(int, input().split())) for _ in range(m))
print(s)

from itertools import combinations

for i in range(n, 0, -1):
    combination = combinations(range(1, n+1), i)
    for comb in combination:
        if not set(combinations(comb, 2)) - s:
            print(i)
            exit()
