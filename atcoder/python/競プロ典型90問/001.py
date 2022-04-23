# 入力
# N：切れ目の個数
# L: 羊羹の全長
# K: N個の切れ目の中から実際に選べる切れ目の数
# A: 切れ目が左から何センチの部分にあるか？

# 方針
# 二分探索
# size(cm)以上のk+1(個)に分けられるかどうかをチェックして範囲を絞っていく

import numpy as np
N, L = map(int, input().split())
K = int(input())
A = np.array([0] + list(map(int, input().split())) + [L])


def check(size):
    cnt = 0
    x = 0
    print("size:", size)
    while x + size <= L:
        x = A[np.searchsorted(A, x + size)]
        print("x:", x)
        cnt += 1
    print(cnt)
    return cnt

ok, ng = 0, L + 1
while ok + 1 < ng:
    x = (ok + ng) // 2
    print("ok+ng/2:", x)
    if (check(x) >= K + 1):
        ok = x
    else:
        ng = x
print(ok)
