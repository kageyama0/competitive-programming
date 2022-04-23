n = int(input())

# 現在の文字:s
# 使える左括弧の数:left
# 使える右括弧の数:right
def dfs(s, left, right):
    # 左括弧と右括弧を使い切った場合に、出力
    if left == right == 0:
        print(s)
        return

    # 左括弧は足す場合
    if left > 0:
        dfs(s + '(', left-1, right)

    # 右括弧を足す場合
    # ただし、左括弧のほうが右括弧よりも使われていなければならない。
    if right > 0 and left < right:
        dfs(s + ')', left, right-1)

if n%2 == 0:
    dfs('', n//2, n//2)
