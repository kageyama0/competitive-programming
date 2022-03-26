N = int(input())
A = list(set(map(int, input().split())))

for i in range(N+1):
    if not i in A:
        print(i)
        exit()
