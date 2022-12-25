# 方針: 全探索
# なぜ、全探索で良いと思えるか？
# 制約が小さいので、全探索できる


# https://docs.python.org/ja/3/library/itertools.html#itertools.product
# ジェネレータ式の入れ子になった for ループとおよそ等価です。
# たとえば product(A, B) は ((x,y) for x in A for y in B) と等価です。
# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111

from itertools import product

N = int(input())


# 左括弧があれば+1, 右括弧があれば-1, 途中で値が負になればNGだし、最後に0になっていなくてもNG
def isvalid(S):
    score = 0
    for c in S:
        if c == '(':
            score += 1
        else:
            score -= 1

        if score < 0:
            return False

    return score == 0


# a = list(product(["(", ")"], repeat=N))
# print(*a, sep="\n")


# 括弧を用いて作ることができるありうる全ての文字列を生成する
for bit in product(["(", ")"], repeat=N):
    # 生成した文字列が有効なものかを判定する
    if (isvalid(bit)):
        print(*bit, sep='')
