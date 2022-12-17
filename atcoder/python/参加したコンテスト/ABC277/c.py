from collections import defaultdict, deque

n = int(input())

# defaultdictを使うことで、キーが存在しないときに自動的に空のリストを返す
graph = defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = deque()
q.append(1)
ans = 1
visited = set()
while q != deque():
    v = q.popleft()
    # print(q, v)

    # 梯子を登った先が行き止まりならスキップ
    if graph[v] == []:
        continue

    # 繋がっているハシゴがあれば、全部登ってみる
    for i in graph[v]:
        if i in visited:
            continue
        ans = max(ans, i)
        q.append(i)
        visited.add(i)

print(ans)
