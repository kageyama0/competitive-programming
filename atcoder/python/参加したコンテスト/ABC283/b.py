n = int(input())
A = [0] + list(map(int, input().split()))
q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        k, x = query[1], query[2]
        A[k] = x

    else:
        k = query[1]
        print(A[k])
