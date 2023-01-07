# こんなもんはDPだが、どうDPしていいか分からない...
# 管理するものがコストだけじゃなくて、開けられる宝箱も管理しないといけない。
# それに宝箱を管理するにしても、1,2,3を100円で開けられる状況と1,2,4を120円で開けられる状況のどっちが良いのかどうやって判断するのか？
# 方針: bitDPらしい

def bit(C):
    tmp = 0
    for i in C:
        tmp += 1 << i - 1
    return tmp


n, m = map(int, input().split())

# dp[i][msk]: i番目の鍵まで見て、開けられる宝箱の集合がmskであるのに必要な費用の最小値
dp = [[float("inf")] * (1 << n) for _ in range(m)]
dp[0][0] = 0
print(dp)

# Aは、i番目の鍵の値段を格納。Bは、i番目の鍵で開けられる宝箱の個数を格納
# Keyは、i番目の鍵で開けられる宝箱の集合を格納
A, B = [0] * (m+1), [0] * (m+1)
Key = [[] for _ in range(m+1)]

for i in range(1, m+1):
    a, b = map(int, input().split())
    A[i], B[i] = a, b

    C = list(map(int, input().split()))
    Key[i] = bit(C)

print(A, B, Key)

for i in range(1, m+1):
    for j in range(1 << n):
        dp[i][j | Key[i]] = min(dp[i][j | Key[i]], dp[i-1][j] + A[i])
