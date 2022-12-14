N, M, K = map(int, input().split())
MOD = 998244353


# 使っている数字の合計と使った数字で出来た配列を入れていく。
# [cnt, A]
# これだと、重複してカウントしてしまうし、時間もかかりすぎる....
q = [[0, [0] * N]]
print(q)
cnt = 1
while q:
    now, A = q.pop()
    print(now, A)
    if now < K - N:
        for i in range(N):
            if A[i] < M:
                q.append([now + 1, A[:i] + [A[i] + 1] + A[i + 1:]])
                cnt += 1

print(cnt % MOD)
