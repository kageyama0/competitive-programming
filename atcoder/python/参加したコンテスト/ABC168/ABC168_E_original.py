from math import gcd
n = int(input())
MOD = 1000000007
d = {}

zero = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == b == 0:
        zero += 1
        continue

    # 最大公約数で割っておく
    g = gcd(a, b)
    a //= g
    b //= g

    if b < 0:
        a *= -1
        b *= -1
    if b == 0 and a == -1:
        a = 1

    if a > 0:
        






# まず、一緒に入れられないイワシを見つける
#

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
