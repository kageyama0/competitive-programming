from collections import deque
r, c = map(int, input().split())
s0, s1 = map(lambda x: int(x) - 1, input().split())
g0, g1 = map(lambda x: int(x) - 1, input().split())

graph = [list(input()) for _ in [0] * r]
graph[s0][s1] = 0
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque([[s0, s1]])

while q:
    x, y = q.popleft()
    for dx, dy in d:
        if graph[x + dx][y + dy] == ".":
            graph[x + dx][y + dy] = graph[x][y] + 1
            q.append([x + dx, y + dy])
    # print(graph)
print(graph[g0][g1])
