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

visited = [False] * (n + 1)
path = []
ans = 0
limit = 10 ** 6

def dfs(c):
    global ans
    if ans == limit:
        return

    visited[c] = True
    path.append(c)
    ans += 1

    for next in graph[c]:
        if visited[next]:
            continue

        dfs(next)

    visited[c] = False
    path.pop()


dfs(1)
print(ans)
