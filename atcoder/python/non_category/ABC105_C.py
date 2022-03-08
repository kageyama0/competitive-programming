# -2進数にする

n = int(input())
ans = []
#now = (-2)^n = 1,-2,4,-8,16....
now = 1
while n != 0:
    if n % (abs(now) * 2) == 0:
        ans.append("0")
    else:
        ans.append("1")
        n -= now

    now *= -2
    #print(n, now, ans)

if ans == []:
    print(0)
else:
    out = ""
    for i in range(len(ans) - 1, -1, -1):
        out += ans[i]

    print(out)
