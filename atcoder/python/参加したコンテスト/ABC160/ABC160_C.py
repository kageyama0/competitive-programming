k, n = map(int, input().split())
a = list(map(int, input().split()))
l = len(a)
dis = [None] * (l - 1)
for i in range(n - 1):
    dis[i] = ans[i + 1] - ans[i]
print(dis)
