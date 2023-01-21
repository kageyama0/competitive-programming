# 操作1: a円払うと、sの左端を右端に持ってくる
# 操作2: b円払うと、sの中の１つの文字を好きな文字に変えられる
# sを回文にするために必要な最小のコストを求める
# 全探索？
# 全部のパターンを試すには？

n, a, b = map(int, input().split())
s = input()
# 左端の文字を右端に持ってくるパターンを全部見てみる
# 操作1をしたやつを全部(1 ~ n-1回)見てみる
ope1 = [None] * n
ope1[0] = s
for i in range(1, n):
    ope1[i] = ope1[i-1][1:] + ope1[i-1][0]

# 最小値は操作２で全部入れ替えるやつ
min_cost = b * n
for i in range(n):
    # 操作1をi回したやつ
    cnt = a * i

    # 両橋から同じじゃない文字を探す
    for j in range(n // 2):
        if ope1[i][j] != ope1[i][n-1-j]:
            cnt += b

    min_cost = min(min_cost, cnt)

print(min_cost)
