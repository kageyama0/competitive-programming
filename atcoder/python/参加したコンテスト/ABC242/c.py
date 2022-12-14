N = int(input())
MOD = 998244353

a = b = c = d = e = 1

for _ in range(N-1):
    a, b, c, d, e = a+b, a+b+c, b+c+d, c+d+e, 2*d + e
    a, b, c, d, e = a % MOD, b % MOD, c % MOD, d % MOD, e % MOD

ans = (2 * (a+b+c+d) + e) % MOD
print(ans)
