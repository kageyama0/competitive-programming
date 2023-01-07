from collections import deque
from sys import stdin
input = stdin.readline
inf = 1 << 60

n, m, k = map(int, input().split())
edges0 = [[] for _ in range(n)]
edges1 = [[] for _ in range(n)]
for _ in range(m):
    u, v, a = map(int, input().split())
    if a:
        edges1[u - 1].append(v - 1)
        edges1[v - 1].append(u - 1)
    else:
        edges0[u - 1].append(v - 1)
        edges0[v - 1].append(u - 1)

switch = [0] * n
for x in map(int, input().split()):
    switch[x - 1] = 1

# BFS
todo = deque()

visited0 = [inf] * n
if switch[0]:
    visited0[0] = 0
    todo.append(0)

visited1 = [inf] * n
visited1[0] = 0
todo.append(1)

while todo:
    print("------------")
    print(f"edges0:{edges0}", f"edges1:{edges1}")
    print(f"visited0:{visited0}")
    print(f"visited1:{visited1}")
    print(todo)
    u, a = divmod(todo.popleft(), 2)
    print(f"u:{u}, a:{a}")
    if a:
        print("a==1")
        for v in edges1[u]:
            if visited1[u] + 1 < visited1[v]:
                visited1[v] = visited1[u] + 1
                todo.append(2 * v + 1)
                if switch[v]:
                    visited0[v] = visited1[v]
                    todo.append(2 * v)
    else:
        for v in edges0[u]:
            if visited0[u] + 1 < visited0[v]:
                visited0[v] = visited0[u] + 1
                todo.append(2 * v)
                if switch[v]:
                    visited1[v] = visited0[v]
                    todo.append(2 * v + 1)


ans = min(visited0[n - 1], visited1[n - 1])
if ans == inf:
    print(-1)
else:
    print(ans)
