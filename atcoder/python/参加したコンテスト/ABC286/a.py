n, p, q, r, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = A[:p] + A[r:s+1] + A[q+1:r] + A[p:q+1] + A[s+1:]
print(*B[1:])
