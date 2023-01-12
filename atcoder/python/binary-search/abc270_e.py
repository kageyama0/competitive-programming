# 方針: m 周したときに食べるりんごの個数は K 個以下か？」という条件で m について二分探索する

n, k = map(int, input().split())
A = list(map(int, input().split()))

# m周した時に食べるりんごの個数がk以下かチェック
def check(m):
    cnt = 0
    for a in A:
        cnt += min(a, m)
    return cnt <= k

# 何周できるか二分探索でチェック
ok, ng = 0, 10 ** 12 + 1
while ng - ok > 1:
    m = (ok + ng) // 2
    if check(m):
        ok = m
    else:
        ng = m


# ok周した時に残っているりんごの個数を計算する
rest = k
for i in range(n):
    sub_cnt = min(A[i], ok)
    A[i] -= sub_cnt
    rest -= sub_cnt

# print(A, rest)

# ok周した後に残っているりんごで前から食べていく
while rest > 0:
    for i in range(n):
        if A[i] == 0:
            continue

        if rest == 0:
            break

        A[i] -= 1
        rest -= 1

print(*A)
