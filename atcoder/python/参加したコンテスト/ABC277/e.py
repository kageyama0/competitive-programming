from collections import defaultdict, deque

n, m, k = map(int, input().split())
graph = [defaultdict(int) for _ in range(n + 1)]
for _ in range(m):
    u, v, a = map(int, input().split())
    if v in graph[u] or u in graph[v]:
        print(-1)
        exit()
    graph[u][v] = a
    graph[v][u] = a

S = list(map(int, input().split()))
# print("S", S)
# print(*graph, sep='\n')

q = deque()
q.append([1, 1, 0])
visited = defaultdict(int)
ans = n * m
while q != deque():
    now, switch_status, point = q.popleft()
    # print(q)
    # print("visited", visited)
    # print("now, switch_status, point", now, switch_status, point)

    # 通った場所とその時のスイッチのオンオフを記録
    visited[now] = switch_status

    # たどり着いた頂点がNなら、最小値だけ計算してスキップ
    if now == n:
        ans = min(ans, point)
        continue

    # たどり着いた頂点が行き止まりならスキップ
    if graph[now] == []:
        continue

    # 繋がっている頂点があれば、全部いってみる
    for next, switch_restriction in graph[now].items():
        # print("---")
        # print("繋がっている頂点にいってみる", f"[{next}]にはswitchがこの状態({switch_restriction})じゃないと通れない")

        # switchを押さないと通れない時
        if switch_restriction != switch_status:
            # スイッチがある時は、通れる(スイッチがない時は、行き止まり
            # print("スイッチがある時は、通れる", "now, next", now, next)
            if now in S:
                # print(f"{now}にはスイッチがあったので、押してみる")
                if next in visited:
                    if visited[next] == (switch_status + 1) % 2:
                        # print("skip", next, switch_restriction)
                        continue

                q.append([next, (switch_status + 1) % 2, point + 1])

            # else:
            #     print(f"{now}にはスイッチがなかった")

        # switchを押さなくても、通れる時
        else:
            # print("switchを押さなくても、通れる時")
            if next in visited:
                if visited[next] == switch_status:
                    # print("skip", next, switch_restriction)
                    continue
            q.append([next, switch_status, point + 1])

    # print("-------------------------")


print(ans if ans != n * m else -1)
