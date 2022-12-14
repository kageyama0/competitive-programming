

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
ans = n * (n + 1) // 2
for i in range(1, n):
    for j in range(i + 1, n + 1):
        ans += gcd(i, j) * 6

for i in range(1, n - 1):
    for j in range(i + 1, n):
        for k in range(j + 1, n + 1):
            x = gcd(i, j)
            ans += gcd(x, k) * 6

print(ans)
