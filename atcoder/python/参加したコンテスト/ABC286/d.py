# 組み合わせなので、dpか？

n, x = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]


dp = [False] * (x + 1)
dp[0] = True

# i番目の硬貨を使って
for i in range(n):
    # 金額, 枚数
    money, money_cnt = AB[i][0], AB[i][1]

    # 金額の大きい順に確認していく
    for j in range(x, -1, -1):

        # 1 ~ money_cnt枚使う
        for k in range(1, money_cnt + 1):
            if j - k * money >= 0:
                # dp[j - k * money]がTrueなら、dp[j]もTrueになる
                # ただし、dp[j]がTrueで、dp[j - k * money]がFalseの場合は、dp[j]はTrueのまま
                dp[j] |= dp[j - k * money]

    # print(dp)

if dp[x]:
    print("Yes")
else:
    print("No")
