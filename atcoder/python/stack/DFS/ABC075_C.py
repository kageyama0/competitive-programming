n, m = map(int, input().split())

g = [[] for i in range(n + 1)]
v = [0] * (n + 1)
e = []
for i in range(m):
    a, b = map(int, input().split())
    e.append((a, b))
    g[a].append(b)
    g[b].append(a)


def dfs(start, end):
    q = []
    q.append(start)

    while q:
        # 現在位置curをスタックに追加
        cur = q.pop()
        # 訪れた場所として記録
        v[cur] = 1

        if cur == end:
            return True

        # 繋がっている頂点next_vをまだ訪れていなければ、qに追加
        # (cur, next_v) != (start, end)は、辺になっていなければ、つまり一旦他の頂点を経由して目的地にたどり着いてしまった場合...
        for next_v in g[cur]:
            if v[next_v] != 1 and (cur, next_v) != (start, end):
                q.append(next_v)
    return False


ans = 0
for a, b in e:
    v = [0] * (n + 1)
    if not dfs(a, b):
        ans += 1

print(ans)
