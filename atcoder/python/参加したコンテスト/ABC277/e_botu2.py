# スイッチが入っている状態と入ってない状態で、
# それぞれ別にedgesとvisitedを管理する

from collections import deque

n, m, k = map(int, input().split())
INF = float("inf")
edges0 = [[] for _ in range(n+1)]
edges1 = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, a = map(int, input().split())
    if a == 1:
        edges1[u].append(v)
        edges1[v].append(u)
    else:
        edges0[u].append(v)
        edges0[v].append(u)

S = [0] * (n+1)
for s_p in list(map(int, input().split())):
    S[s_p] = 1

q = deque()
visited0 = [INF] * (n+1)
# スタート地点にスイッチがある時
if S[1] == 1:
    visited0[1] = [0]
    q.append((1, 0))

visited1 = [INF] * (n+1)
visited1[1] = 0
q.append((1, 1))

while q:
    print("------------")
    print(q)
    print(f"edges0:{edges0}", f"edges1:{edges1}")
    print(f"visited0:{visited0}")
    print(f"visited1:{visited1}")
    now, switch = q.popleft()

    if switch == 0:
        for next in edges0[now]:
            # 最短距離で来れた場合にのみ、qに追加
            if visited0[now] + 1 < visited0[next]:
                visited0[next] = visited0[now] + 1
                q.append((next, 0))
                if S[next] == 1:
                    visited1[next] = visited0[next]
                    q.append((next, 1))

    elif switch == 1:
        for next in edges1[now]:
            # 最短距離で来れた場合にのみ、qに追加
            if visited1[now] + 1 < visited1[next]:
                visited1[next] = visited1[now] + 1
                q.append((next, 1))
                if S[next] == 1:
                    visited0[next] = visited1[next]
                    q.append((next, 0))

ans = min(visited0[n], visited1[n])
if ans == INF:
    print(-1)
else:
    print(ans)
