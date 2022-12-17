n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

for i in range(1, n+1):
    d = len(graph[i])
    if d == 0:
        print(0)
        continue
    else:
        g = sorted(graph[i])
        print(d, *g)
