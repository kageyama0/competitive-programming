from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
par = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

visited = [0] + [1] + [0] * (n-1)
q = deque()
q.append(1)
while q:
    now = q.popleft()
    #print("now:", now)
    visited[now] = 1
    for next in G[now]:
        #print("next:", next)
        #print("visited:", visited)
        if visited[next]:
            continue
        q.append(next)
        par[next] = now
        visited[next] = 1
print("Yes")
print("\n".join(map(str, par[2:])))
