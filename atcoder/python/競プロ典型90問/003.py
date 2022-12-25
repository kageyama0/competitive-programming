# 条件
# 都市: N個, 道路: (N-1)本, 新しく立てられる道路: 1本
# 同じ道は通れない!

# 求めるもの
# ある都市から出発して元に戻ってくるまでの道路の長さの最大値

# 方針: 木構造の性質を利用する
# ・ 木構造の性質
#   1. 木構造は、N個の頂点とN-1本の辺からなる
#   2. 木構造は、任意の2頂点間に1つのパス(単純パス)が必ず存在する
#   3. 任意の2頂点間を直接結ぶと、閉路が1つできる
# これを知っていれば、あとは単純パスの最大値を求めればいいだけになる


import numpy as np

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

# まずは、始点である1から一番遠い点を求める。
# やり方としては、上で作ったgraphを使って、今いる地点と繋がっているところに行き、行くたびに距離を1増やしていく。
# その際、行ったことのあるところには行かないようにするために、行ったことのあるところをrankとして記録しておく。
rank = np.array([-1]*(n+1))
rank[1] = 0
q = [1]
while q:
    now = q.pop()
    print("now:", now)
    for next in graph[now]:
        print("next:", next)
        print("rank", rank)
        if rank[next] >= 0:
            continue
        q.append(next)
        rank[next] = rank[now] + 1

max_rank_index = np.argmax(rank)
print(rank, max_rank_index)


# 次に、点1から一番離れた点を始点として、そこから一番離れた点を探す。
rank = np.array([-1]*(n+1))
rank[max_rank_index] = 0
q = [max_rank_index]
while q:
    now = q.pop()
    print("now:", now)
    for next in graph[now]:
        print("next:", next)
        print("rank", rank)

        if rank[next] >= 0:
            continue
        q.append(next)
        rank[next] = rank[now] + 1

ans = np.amax(rank) + 1
print(ans)
