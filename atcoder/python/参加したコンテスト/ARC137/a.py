# 全探索するにはとても大きい数字を扱うことになると思ったが、
# 答えとして考えられる最大値を取る組み合わせから探索して行って見つけた時点で
# 答えを出力すれば良いのか〜

from math import gcd

L, R = map(int, input().split())

for ans in range(R - L, 0, -1):
    for l in range(L, R+1):
        if l + ans > R:
            break
        if gcd(l,l+ans) == 1:
            print(ans)
            exit()
