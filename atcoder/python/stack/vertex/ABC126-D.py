# https://atcoder.jp/contests/abc126/submissions/7966715
N = int(input())

link = [[] for _ in range(N)]
# 頂点同士の距離を記録す
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    link[u - 1].append((v - 1, w))
    link[v - 1].append((u - 1, w))
    # print(link)

# dに頂点１(インデックスは0)からの距離を記録していく
d = [-1] * N
d[0] = 0
q = [0]
# 次に距離を記録するインデックスを記録
while q:
    i = q.pop()
    for n, w in link[i]:
        # まだ記録していないやつなら
        if d[n] == -1:
            d[n] = d[i] + w
            q.append(n)
    print(d)

for i in d:
    print(i % 2)
