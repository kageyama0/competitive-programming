t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    # 配列内の奇数をカウントする
    cnt = 0
    for i in range(n):
        if A[i] % 2 == 1:
            cnt += 1
    print(cnt)
