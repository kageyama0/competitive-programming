n = int(input())

# 文字が7,5,3すべてを含んでいたら １ を返し、その数字にまた7,5,3をつけた数字をこの関数に渡す


def dfs(s):

    if int(s) > n:
        return 0

    if all(s.count(c) > 0 for c in ["7", "5", "3"]):
        ret = 1
    else:
        ret = 0

    for c in ["7", "5", "3"]:
        ret += dfs(s + c)

    # print(s,ret)
    return ret


print(dfs("0"))
