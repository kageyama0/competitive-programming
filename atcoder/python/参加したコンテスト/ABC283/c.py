s = input()

n = len(s)

ans = 0
now_0 = 0
for i in range(n):
    si = s[i]
    if si == "0":
        now_0 += 1
        if now_0 == 2:
            now_0 = 0
            ans += 1
        else:
            pass

    else:
        if now_0 == 1:
            now_0 -= 1
            ans += 2

        elif now_0 == 0:
            ans += 1

if now_0 == 1:
    ans += 1

print(ans)
