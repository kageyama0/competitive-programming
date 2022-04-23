# bit全探索

from itertools import product
N = int(input())


def isvalid(S):
    score = 0
    for c in S:
        if c == '(':
            score += 1
        else:
            score -= 1

        # 途中で 0 を下回るとダメ
        if score < 0:
            return False

    # 最後に 0 なら True、そうでなければ False
    return (score == 0)


# a = list(product(["(", ")"], repeat=N))
# print(*a, sep="\n")

for bit in product(["(", ")"], repeat=N):
    if (isvalid(bit)):
        # リストを文字列に
        print(*bit, sep='')
