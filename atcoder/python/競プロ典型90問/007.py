# https://atcoder.jp/contests/typical90/tasks/typical90_g
# 方針: 二分探索
# https://docs.python.org/ja/3/library/bisect.html

from bisect import bisect_left as bl

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()
INF = 1 << 60
A = [-INF] + A + [INF]


for _ in range(Q):
    b = int(input())
    R = bl(A, b)
    L = R - 1

    dif_x = A[R]-b
    dif_y = b - A[L]

    print(min(dif_x, dif_y))
