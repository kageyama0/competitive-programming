# ４文字の中で前後を入れ替えて見て　AGCが入っていればTrue
def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]

        if ''.join(t).count('AGC') >= 1:
            return False

    return True

# cur:現在の文字数、last3:最後３文字
def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]

    if cur == n:
        return 1

    ret = 0
    for c in 'ACGT':
        if ok(last3 + c):
            ret = (ret + dfs(cur + 1, last3[1:] + c)) % MOD

    memo[cur][last3] = ret
    return ret


def main():
    global n, MOD, memo
    n = int(input())
    MOD = 10 ** 9 + 7
    ans = 4 ** n
    memo = [{} for i in range(n + 1)]
    print(dfs(0, '...'))


if __name__ == "__main__":
    main()
