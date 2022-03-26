N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [set() for _ in range(N)]
dp[0] = [A[0], B[0]]

for i in range(1,N):
    a = A[i]
    b = B[i]
    for x in dp[i-1]:
        if abs(x-a) <= K:
            dp[i].add(a)
        if abs(x-b) <= K:
            dp[i].add(b)

    # print(dp[i])
    if dp[i] == set():
        print("No")
        exit()

print("Yes")
