# https://atcoder.jp/contests/abc146/tasks/abc146_c
# 方針 : 二分探索
# 答えがある一つの値に決まることがわかっているので、二分探索を行う

def calc(n):
    return a * n + b * len(str(n))


a, b, x = map(int, input().split())
ok, ng = 0, 10 ** 9 + 1
while ok + 1 < ng:
    # print(ok, ng)
    mid = (ok + ng) // 2
    if calc(mid) <= x:
        ok = mid
    else:
        ng = mid

print(ok)
