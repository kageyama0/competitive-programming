from collections import Counter
from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))
# print(A)
c = dict(Counter(A))
print(c)
# cnt = 0
# for i in range(N):
#     for j in range(i, N):
#         x = A[i] * A[j]
#         if x in A:
#             # print("i,j", i, j, " ", A[i], A[j], x)
#             if i != j:
#                 cnt += 2 * c[x]
#             else:
#                 cnt += c[x]

# print(cnt)

cnt = 0
# 1だけ特殊なので、1の場合だけ別でカウントする。
# Ai, Aj, Akが全て１の場合、１の個数c[1]から３つ取り出す重複組みわせを考える.n+r-1Cr
cnt += cmb(c[1]+2, 3)
print(cnt)

# Aj or Akが1の場合、Ai が Aj or Akと等しくなる
# そうすると、1とそれ以外の数から２こ取り出す重複組み合わせを考える.
for v in c.values():
    cnt += cmb(v+1, 2) * c[1] * 2
print(cnt)


# Aiが平方数の場合を数える。
for k, v in c.items():
    z = k * k
    z_cnt = c.get(z, 0)
    cnt += cmb(v+1, 2) * z_cnt
print(cnt)


# それ以外の場合、
B = [k for k in c.keys()]
B.sort()
l = len(B)
for i in range(1, l):
    for j in range(i+1, l):
        x, y = B[i], B[j]
        z = x*y
        z_cnt = c.get(z, 0)
        cnt += z_cnt * c[x] * c[y] * 2


print(cnt)
