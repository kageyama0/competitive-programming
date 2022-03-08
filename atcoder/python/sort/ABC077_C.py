import bisect

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort()
b.sort()
c.sort()

ans = 0

for middle in b:
    # 挿入できる箇所の左側のインデックスを返す
    tmp1 = bisect.bisect_left(a, middle)
    # 挿入できる箇所の右側のインデックスを返す
    tmp2 = bisect.bisect_right(c, middle)
    ans += tmp1 * (n - tmp2)

print(ans)
