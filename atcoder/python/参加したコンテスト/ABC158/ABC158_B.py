n, a, b = map(int, input().split())

l = a + b
set_cnt = n // l
rest = n % l
if rest >= a:
    ans = set_cnt * a + a
else:
    ans = set_cnt * a + rest

print(ans)
