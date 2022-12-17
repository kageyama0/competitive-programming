n, t = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)
rest = t % s

for i in range(n):
    if rest >= A[i]:
        rest -= A[i]
    else:
        print(i+1, rest)
        exit()
