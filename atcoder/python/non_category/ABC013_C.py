n, hp = map(int, input().split())
a, b, c, d, e = map(int, input().split())
ans = 10 ** 9
for xy in range(n):
    for x in range(xy + 1):
        y = xy - x
        sat = x * b + y * d + hp - (n - xy) * e
        if sat >= 0:
            cost = x * a + y * c
            ans = min(ans, cost)
print(ans)
