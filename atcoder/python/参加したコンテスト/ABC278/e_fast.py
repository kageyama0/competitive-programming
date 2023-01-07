# https://atcoder.jp/contests/abc278/tasks/abc278_e
# imos法を使う
# 参考:
# TODO: 後でやり直す

H, W, N, h, w = map(int, input().split())

K, L = H + 2 - h, W + 2 - w
P = [[1, K, 1, L] for _ in range(N)]  # [a-1]=[ks,kt,ls,lt]

for i in range(2, H+2):
    for j, a in enumerate(map(int, input().split()), 2):
        a -= 1
        P[a][0] = max(P[a][0], i-h)  # ks
        P[a][1] = min(P[a][1], i)  # kt
        P[a][2] = max(P[a][2], j-w)  # ls
        P[a][3] = min(P[a][3], j)  # lt

imos = [[0]*(L+1) for _ in range(K+1)]

for ks, kt, ls, lt in P:
    if ks < kt and ls < lt:
        imos[ks][ls] -= 1
        imos[kt][lt] -= 1
        imos[ks][lt] += 1
        imos[kt][ls] += 1

imos[1][1] += N
for k in range(1, K):
    for l in range(1, L):
        imos[k][l] += imos[k][l-1] + imos[k-1][l] - imos[k-1][l-1]
    print(' '.join(map(str, imos[k][1:L])))
