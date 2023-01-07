from collections import Counter, defaultdict

H, W, N, h, w = map(int, input().split())

cnt = defaultdict(int)
grid = [[None] * W for _ in range(H)]
for i in range(H):
    A = list(map(int, input().split()))
    for a in A:
        cnt[a] += 1
    grid[i] = A

# print(cnt, grid)

num_type = len(cnt)

# 0 ≤ k ≤ H−h, 0 ≤ l ≤ W−wで囲まれた範囲の数字の種類を数えて、全体からひく
for k in range(H - h + 1):
    ANS = []
    for l in range(W - w + 1):

        # 0 ≤ k ≤ H−h, 0 ≤ l ≤ W−wで囲まれた範囲の数字の種類を数える
        c = defaultdict(int)
        for i in range(h):
            for j in range(w):
                c[grid[k + i][l + j]] += 1
        # print(c)

        # 全体で持っている数字の種類の数と、範囲内の数字の種類の数が同じなら１つ種類が減ったことになる
        kl_cnt = num_type
        for num, count in c.items():
            if cnt[num] == count:
                kl_cnt -= 1
        ANS.append(kl_cnt)
    print(*ANS)
