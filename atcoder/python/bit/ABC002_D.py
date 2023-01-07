# https://www.sejuku.net/blog/23318
import itertools

n, m = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


MAX = 0
# 1をnだけ左にずらす
# ex) 1<<4 = b10000 = 16
#     0 ~ (1<<n - 1) = 15
for bit in range(1 << n):
    lis = []
    for i in range(n):
        mask = 1 << i
        if bit & mask:
            lis.append(i + 1)
    #print(bit, lis)

    for x, y in itertools.combinations(lis, 2):
        if not graph[x][y]:
            break
    else:
        MAX = max(MAX, len(lis))
print(MAX)
