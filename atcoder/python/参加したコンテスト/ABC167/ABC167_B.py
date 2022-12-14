a, b, c, k = map(int, input().split())

ans = 0
if a >= k:
    ans += k
else:
    ans += a
    k -= a
    if b >= k:
        ans += k
    else:
        ans += b
        k -= b
        if c >= k:
            ans -= k
        else:
            ans -= c
print(ans)
