h, w = map(int, input().split())
ans = 0
for _ in range(h):
    s = input()
    ans += s.count("#")
print(ans)
