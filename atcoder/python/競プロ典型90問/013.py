# https://atcoder.jp/contests/typical90/tasks/typical90_m
# ダイクストラやん
# 両橋からダイクストラするって発想がなかった...

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start_node):
    COST = [float("inf")] * (n+1)
    COST[start_node] = 0
    q = deque()
    # q: [(cost, node), ... ]
    q.append((0, start_node))
    while q:
        now_cost, now_node = q.popleft()

        # 次に行けるノードとそのためのコストを取得
        for next_node, to_next_cost in graph[now_node]:

            # 今のコストと、今のノードから次のノードに行くためのコストを足したものが、
            # 次のノードのコストよりも小さければ更新し、キューに追加
            if COST[next_node] > now_cost + to_next_cost:
                COST[next_node] = now_cost + to_next_cost
                q.append((now_cost + to_next_cost, next_node))

    return COST

# 1から各ノードへの最短距離, nから各ノードへの最短距離
start_cost = dijkstra(1)
end_cost = dijkstra(n)
# print(start_cost, end_cost)

for k in range(1, n+1):
    start_k_cost = start_cost[k]
    k_end_cost = end_cost[k]
    print(start_k_cost + k_end_cost)
