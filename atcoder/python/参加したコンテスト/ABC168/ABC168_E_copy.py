# coding: utf-8
# Your code here!
# https://atcoder.jp/contests/abc168/submissions/13322207

from math import gcd
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, *ab = [int(i) for i in read().split()]
# n   --> 10
# ab  --> [3, 2, 3, 2, -1, 1, 2, -1, -3, -9, -8, 12, 7, 7, 8, 1, 8, 2, 8, 4]
# *ab --> 3 2 3 2 -1 1 2 -1 -3 -9 -8 12 7 7 8 1 8 2 8 4
M = iter(ab)
d = {}

zero = 0
for a, b in zip(M, M):
    if a == b == 0:
        zero += 1
        continue
    g = gcd(a, b)
    a //= g
    b //= g
    if b < 0:
        a = -a
        b = -b
    if b == 0 and a == -1:
        a = 1

    if a > 0:
        if (a, b) in d:
            d[(a, b)][0] += 1
        else:
            d[(a, b)] = [1, 0]
    else:
        if (b, -a) in d:
            d[(b, -a)][1] += 1
        else:
            d[(b, -a)] = [0, 1]


MOD = 1000000007
ans = 1

pow2 = [1]
for _ in range(200005):
    pow2.append(pow2[-1]*2 % MOD)

#print(d)
for (a, b), (k, l) in d.items():
    ans *= pow2[k]+pow2[l]-1
    ans %= MOD

ans += zero-1
print(ans % MOD)




# from itertools import combinations

# n = int(input())
# AB = [[]] + [list(map(int, input().split())) for _ in range(n)]
# MOD = 1000000007
# # まず、一緒に入れられないイワシを見つける
# #

# d_comb = []
# for i in range(1, n):
#     for j in range(i + 1, n+1):
#         #print(i,j,AB)
#         Ai, Bi = AB[i][0], AB[i][1]
#         Aj, Bj = AB[j][0], AB[j][1]
#         if Ai * Aj == -Bi * Bj:
#             d_comb.append({i, j})
# print(d_comb)

# cnt = 0
# for i in range(n, 0, -1):
#     combination = combinations(range(1, n+1), i)
#     for comb in combination:
#         for d in d_comb:
#             if not d <= set(comb):
#                 cnt += 1
# print(cnt)
