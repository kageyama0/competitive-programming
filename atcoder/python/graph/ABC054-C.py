n, m = map(int, input().split())
s = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for i in range(n):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

print(s)
