n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

# ループを見つけに行けばイ


def loop(now, town):
    cnt = 0
    while True:
        # print(now)
        next = a[now]
        if town[next] == 1:
            cnt += 1
            break
        else:
            town[next] = 1
            now = next
            cnt += 1
    return cnt, now


def tp(num, now):
    for _ in range(num):
        next = a[now]
        now = next
    return next


town1 = [None] + [0] * n
town1[1] = 1
loop1, now1 = loop(1, town1)

town2 = [None] + [0] * n
town2[now1] = 1
loop2, now2 = loop(now1, town2)

if k <= loop1 + loop2:
    ans = tp(k, 1)
else:
    k -= loop1
    k %= loop2
    if k == 0:
        ans = now2
    else:
        ans = tp(k, now2)

print(ans)
