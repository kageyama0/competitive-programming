n,m = map(int,input().split())

# 余ってる c の数
dif = m - 2 * n

# すでにある s に対して、 c の数が足りない時
if dif < 0:
    ans = m // 2

else:
    ans = n + dif // 4

print(ans)
