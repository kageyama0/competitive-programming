N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# Y以上X以下の数字だけでできた配列Bで何通りの部分配列が答えになるか
def calc(B):
    left, right, countX, countY, res = 0, 0, 0, 0, 0

    while left != len(B):
        # 右端までの間に最小値Y、最大値Xである値をカウントする。最小値・最大値どちらも見つかればbreak
        while right != len(B) and (countX == 0 or countY == 0):
            if B[right] == X:
                countX += 1
            if B[right] == Y:
                countY += 1
            right += 1

        # X,Yがどちらもあれば、resに追加
        if countX > 0 and countY > 0:
            res += len(B) + 1 - right

        if B[left] == X:
            countX -= 1
        if B[left] == Y:
            countY -= 1

        # 左端を移動
        left += 1
    return res


left, ans = 0, 0
while left != N:
    B = []
    # NGの数字に当たるまで左端を移動させる
    while left != N and Y <= A[left] <= X:
        B.append(A[left])
        left += 1

    # NGじゃない数字があれば、そこで計算
    if len(B) != 0:
        ans += calc(B)
    else:
        left += 1
print(ans)
