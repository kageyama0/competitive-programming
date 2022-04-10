N, K = map(int, input().split())
A = list(map(int, input().split()))

# 不可能なパターン
if min(A[:K]) > max(A[K:]):
    print(-1)
    exit()

m = float("inf")
# 右から見ていって、それまでの最小値より大きい値は無視しても良いので、-1にしておいて良い
for i in reversed(range(K)):
    if m > A[i]:
        m = A[i]
    else:
        A[i] = -1

end = K
ans = N
for i in range(K):
    if not A[i] == -1:
        for j in range(end, N):
            if A[j] > A[i]:
                ans = min(ans, j - i)
                end = j
                break

print(ans)
