n, k = map(int, input().split())
MOD = 10**9 + 7

A = [0] * (k + 1)
for d in range(1, k + 1):
    # k // d の n 乗をMODで割ったあまり
    A[d] = pow(k // d, n, MOD)

print(A)

for d in range(k, 0, -1):
    for i in range(2, k // d + 1):
        A[d] -= A[d * i]
print(A)

answer = sum(d * x for d, x in enumerate(A))
print(answer % MOD)
