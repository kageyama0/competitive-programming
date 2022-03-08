import math

# n個のブロック,色 m種類, 隣り合うブロックの組であって同じ色で塗られている組がk組以下
n, m, k = map(int, input().split())
MOD = 998244353
ans = 0
for i in range(k + 1):
    a = pow(m - 1, n - i - 1, MOD) % MOD

    c = math.comb(n - 1, k)

    ans += (a * m * c) % MOD
    #print(ans)

print(ans % MOD)
