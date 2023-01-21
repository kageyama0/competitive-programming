# ダイクストラ的な発想？
from collections import deque

def dijkstra(start_node):
    # 到達するためのコスト, お土産の価値
    COST = [(float("inf"), -float('inf'))] * (n+1)
    COST[start_node] = (0, 0)
    q = deque()
    # q: [(cost, value, now_node), ... ]
    q.append((0, A[start_node], start_node))
    while q:
        # print(q)
        now_cost, now_value, now_node = q.popleft()

        # 次に行けるノードを取得
        for next_node in graph[now_node]:

            # print("COST:{}, now_node: {}, next_node: {}".format(COST, now_node, next_node))
            next_node_cost, next_node_value = COST[next_node][0], COST[next_node][1]

            # 直行便がより少ない方
            if next_node_cost > now_cost + 1:
                next_node_value = now_value + A[next_node]
                COST[next_node] = (now_cost + 1, next_node_value)
                q.append((now_cost + 1, next_node_value, next_node))

            # お土産をより多く持っていける方
            elif next_node_cost == now_cost + 1:
                if next_node_value < now_value + A[next_node]:
                    next_node_value = now_value + A[next_node]
                    COST[next_node] = (now_cost + 1, next_node_value)
                    q.append((now_cost + 1, next_node_value, next_node))

    return COST

n = int(input())
A = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for a in range(1, n+1):
    S = [0] + list(input())
    for b in range(1, n+1):
        if S[b] == "Y":
            graph[a].append(b)

# print(graph)

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    # print(dijkstra(u))
    cost, value = dijkstra(u)[v]
    if cost == float("inf"):
        print("Impossible")
    else:
        print(cost, value)
