# トポロジカルソート, topological sort

from collections import defaultdict
import heapq

N, M = map(int, input().split())

# この配列の中身は不変で良いので、listではなくtupleを使った方が親切かも
AB = [tuple(map(int, input().split())) for _ in range(M)]


in_cnt = defaultdict(int)
outs = defaultdict(list)
for a, b in AB:
    in_cnt[b] += 1
    outs[a].append(b)
# print(in_cnt, outs)


# 入次数が0の頂点を追加する
queue = [i for i in range(1, N+1) if in_cnt[i] == 0]
heapq.heapify(queue)

ans = []
while queue:
    # 入次数が0の頂点を小さい順に取り出す
    v = heapq.heappop(queue)
    ans.append(v)

    for v2 in outs[v]:
        in_cnt[v2] -= 1
        if in_cnt[v2] == 0:
            heapq.heappush(queue, v2)


if len(ans) == N:
    print(" ".join(map(str, ans)))
else:
    print(-1)
    exit()
