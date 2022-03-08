n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(m)]
#print(A, B)

for i in range(n - m + 1):
    for j in range(n - m + 1):
        ok = True
        for k in range(m):
            if A[i + k][j:j + m] != B[k]:
                ok = False
                break
        if ok:
            print("Yes")
            exit()
print("No")
