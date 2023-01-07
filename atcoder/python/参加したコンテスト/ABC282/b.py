from itertools import combinations

n, m = map(int, input().split())

A = []
for i in range(n):
    A.append(input())

N = [i for i in range(n)]
comb = combinations(N, 2)
ans = 0
for i, j in comb:
    flag = True
    for x in range(m):
        if A[i][x] == "x" and A[j][x] == "x":
            flag = False
            break

    if flag:
        ans += 1

print(ans)
