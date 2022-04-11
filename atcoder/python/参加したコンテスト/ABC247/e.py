# from itertools import accumulate

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


# diff = [None] * N
# diff[0] = 0
max_index = []
min_index = []
for i in range(N):
    # if i != 0:
    #     diff[i] = A[i] - A[i-1]

    if A[i] == X:
        max_index.append(i)
    if A[i] == Y:
        min_index.append(i)

# print(max_index, min_index)
# print(diff)

# diff = list(accumulate(diff))

cnt = 0
for a in max_index:
    for b in min_index:
        L, R = min(a,b), max(a,b)

        M = A[a]
        m = A[b]
        for num in A[L:R+1]:
            if num > M or num < m:
                break
        cnt += 1

print(cnt)
