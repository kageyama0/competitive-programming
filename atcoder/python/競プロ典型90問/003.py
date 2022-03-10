import numpy as np

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# まずは、始点である1から一番遠い点を求める。
rank = np.array([-1]*(n+1))
rank[1] = 0
q = [1]
while q:
    now = q.pop()
    # print("now:", now)
    for next in graph[now]:
        # print("next:", next)
        # print("rank", rank)
        if rank[next] >= 0:
            continue
        q.append(next)
        rank[next] = rank[now] + 1

max_rank_index = np.argmax(rank)
# print(rank, max_rank_index)


# 次に、点1から一番離れた点を始点として、そこから一番離れた点を探す。
rank = np.array([-1]*(n+1))
rank[max_rank_index] = 0
q = [max_rank_index]
while q:
    now = q.pop()
    # print("now:", now)
    for next in graph[now]:
        # print("next:", next)
        # print("rank", rank)

        if rank[next] >= 0:
            continue
        q.append(next)
        rank[next] = rank[now] + 1

ans = np.amax(cnt) + 1
print(ans)
