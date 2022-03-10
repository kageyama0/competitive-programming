h, w = map(int, input().split())

A = [None]*(h)
rows = [0]*(h)
for i in range(h):

    nums = list(map(int, input().split()))
    rows[i] = sum(nums)
    A[i] = nums

columns = [0]*(w)
for i in range(w):
    cnt = 0
    for j in range(h):
        cnt += A[j][i]
    columns[i] = cnt

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(rows[i] + columns[j] - A[i][j])
    print(" ".join(map(str,ans)))
