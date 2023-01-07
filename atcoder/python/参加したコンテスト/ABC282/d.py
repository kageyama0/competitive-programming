# グラフ
# ２部グラフ
from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

# print(G)

# 色を前から決めていく。直接繋がってるところは隣と違う色にする
C = [-1] * (n+1)
q = deque()
q.append((1, 0))
while q:
    now, color = q.popleft()
    for next in G[now]:
        # まだ色が決まっていないなら、隣と違う色にする
        if C[next] == -1:
            C[next] = 1 - color
            q.append((next, 1-color))

        # 同じ色の頂点が隣接してしまったら、２部グラフではないので終了
        elif C[next] == color:
            print(0)
            exit()

# print(C)

if -1 in C[1:n+1]:
    print(0)
    exit()

# あとは、直接繋がっていない奴らの組み合わせを探して、色が違うやつを数える
ans = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if C[i] != C[j] and j not in G[i]:
            ans += 1
print(ans)
