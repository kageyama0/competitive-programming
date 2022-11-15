# https://atcoder.jp/contests/typical90/tasks/typical90_a

# 入力
# N：切れ目の個数
# L: 羊羹の全長
# K: N個の切れ目の中から実際に選べる切れ目の数
# A: 切れ目が左から何センチの部分にあるか？

# 方針
# 二分探索
# size(cm)以上のk+1(個)に分けられるかどうかをチェックして範囲を絞っていく
# Lcmから順番に調べても良いけど、二分探索の方が早いから、使う
# チェックする方法は、ソートされた配列にこれまた二分探索で、これくらいのサイズの切れ目を入れたらどこに入るか？をチェックしていく。

# なんでこの方針を立てられるのか？
# 答えの範囲が鼻から明らかであること
# その上で、その範囲を狭めていく時に計算量を減らす方法が二分探索であること

import numpy as np

N, L = map(int, input().split())
K = int(input())
A = np.array([0] + list(map(int, input().split())) + [L])


def check(size):
    cnt = 0
    x = 0
    print("size:", size)
    while x + size <= L:
        print("x+size:", x+size)
        print("searchsorted", np.searchsorted(A, x + size))
        # sizeが最小の切れ目なので、二分探索で切れ目が入って欲しい場所の少なくとも右に切れ目があれば、size以上の切れ目が入る
        # 逆にそれより左に切れ目を入れると、size以下の長さになってしまう。
        # 切れそうなところで切れ目を入れて、またその切れ目からsize離れたところに切れ目が入りそうか繰り返す。
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
