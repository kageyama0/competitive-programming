from math import gcd

n = int(input())
A = list(map(int, input().split()))
factorize_A = [[] for _ in range(n)]


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


# 全ての要素が同じなら操作の必要がない
if len(set(A)) == A.count(A[0]):
    print(0)
    exit()

# 最大公約数を求める
g = A[0]
for i in range(1, n):
    g = gcd(g, A[i])

ans = 0
# それぞれの要素を因数分解する
for i in range(n):
    factorize_Ai = prime_factorize(A[i]//g)
    # 2,3以外の要素があれば、操作できないので-1を出力
    for x in factorize_Ai:
        if x != 2 and x != 3:
            print(-1)
            exit()

    ans += len(factorize_Ai)

print(ans)
