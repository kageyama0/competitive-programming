# https: // atcoder.jp/contests/abc165/tasks/abc165_c

from itertools import combinations_with_replacement
# n個の数列、1~mの中で数列を作る
# 2<=n<=10
# 1<=m<=10
n, m, q = map(int, input().split())

comb = combinations_with_replacement(range(1, m + 1), n)
abcd = [list(map(int, input().split())) for _ in [0] * q]

ans = 0
for A in comb:
    cnt = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            cnt += d
    ans = max(ans, cnt)

print(ans)


# ----------maspyさんの早いやつ-----------------
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# N, M, Q = map(int, readline().split())

# A = np.array(list(itertools.combinations_with_replacement(range(1, M + 1), N)))
# n = len(A)
# score = np.zeros(n, np.int32)
# m = map(int, read().split())
# for a, b, c, d in zip(m, m, m, m):
#     cond = A[:, b - 1] - A[:, a - 1] == c
#     score += d * cond
#     print(cond, score)

# print(score.max())
