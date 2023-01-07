# https://atcoder.jp/contests/abc284/tasks/abc284_e
# 無向グラフ、単純パス
# 単純パスの長さを計測しながら、DFS?

from collections import deque, defaultdict

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)

cnt = 1
q = deque()
q.append([1, [1]])
while q and cnt <= 10 ** 6:
    now, visited = q.popleft()

    all_visited = True
    for next in graph[now]:
        if not next in visited:
            cnt += 1
            all_visited = False
            new_visited = visited + [next]
            q.append([next, new_visited])


print(cnt)
