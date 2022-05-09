H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
if R == 1 or R == H:
    if R == 1 == H:
        pass
    else:
        ans += 1

else:
    ans += 2

if C == 1 or C == W:
    if C == 1 == W:
        pass
    else:
        ans += 1

else:
    ans += 2

print(ans)
