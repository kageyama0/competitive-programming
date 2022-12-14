# 入れ替えるのにソートを使う

n, k = map(int, input().split())
A = list(map(int, input().split()))
# 実現すべき配列

#　kまでで良い。
for i in range(k):
    # Aのi , i + k, i + 2k, i + 3k をソートしたものをソートしたものに入れ替えていく
    A[i::k] = sorted(A[i::k])

B = sorted(A)
print("Yes" if A == B else "No")
