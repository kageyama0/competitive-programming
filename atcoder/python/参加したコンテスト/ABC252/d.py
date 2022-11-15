# 自分なりにやったがTLE
# そりゃそうか...DPのつもりやったけど、これ何もカウントしてない。そのままやっただけw


n = int(input())
A = list(map(int, input().split()))

dp = [[] for _ in range(n)]

# 1番目の文字を選んだ場合と選ばなかった場合
dp[0].append(set([A[0]]))
dp[0].append(set())

cnt = 0
for i in range(1, n):
    a_i = A[i]
    # print(f"dp[i-1]:{dp[i-1]}")

    for j in range(len(dp[i-1])):
        # すでに数字を3つ集めていたら、これ以上dpに登録しておかない
        if len(dp[i-1][j]) == 3:
            cnt += 1

        else:
            # 数字a_iがそれまでに選んだ数字と被りがない数字であれば、数字a_iを追加
            if a_i not in dp[i-1][j]:
                dp[i].append(dp[i-1][j].union(set([a_i])))

            # 被りがある場合は、a_iを追加しない
            dp[i].append(dp[i-1][j])

# print(cnt)

# dpの最後に残っているやつの中で長さが3のものを数える
for i in range(len(dp[-1])):
    if len(dp[-1][i]) == 3:
        cnt += 1

print(cnt)
