from collections import deque

n, x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = [0] * (n + 1)
for i in range(n):
    if i + 2 <= n:
        graph[i + 1].append(i + 2)

    if i + 1 == x:
        graph[i + 1].append(y)

print(graph)

q = deque()
for i in range(1, n + 1):
    q.append(i)
    dis = 1
    while q:
        now = q.pop()
        ans[dis] += 1
        dis += 1
        for g in graph[now]:
            q.append(g)
        print(q, ans)

print(ans)

#deque([]) [0, 10, 9, 8, 7, 5, 3, 1, 0, 0, 0]
# 10
# 12
# 10
# 8
# 4
# 1
# 0
# 0
# 0
