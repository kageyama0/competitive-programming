# Union Find
n, m = map(int, input().split())
p = [0] + list(map(int, input().split()))
root = list(range(n + 1))
depth = [0] * (n + 1)


def find_root(x):
    """
    連結成分を作る
    """
    y = root[x]
    if x == y:
        return y
    z = find_root(y)
    root[x] = z
    return z


def merge(x, y):
    xx = find_root(x)
    yy = find_root(y)
    if xx == yy:
        return
    if depth[xx] > depth[yy]:
        root[yy] = xx
    elif depth[xx] < depth[yy]:
        root[xx] = yy
    else:
        root[xx] = yy
        depth[xx] += 1


for _ in range(m):
    x, y = map(int, input().split())
    merge(x, y)
    print("root:", root)
    print("depth:", depth)

# 同じグループにいたら好きに入れ替えられる
# p[i]とiが同じ連結成分にあると1点
ans = 0
for i, x in enumerate(p[1:], 1):
    if find_root(i) == find_root(x):
        ans += 1

print(ans)
