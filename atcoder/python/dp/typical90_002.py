n = int(input())

# nが奇数の場合、出力できるカッコはない
if n % 2 == 1:
    print("")

# 制約がn<=20なので,21ループ
dp = [set() for _ in range(21)]
dp[0].add("")

for i in range(2, 10, 2):
    # https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python
    # |= : これは、setに新しい項目を追加する方法。ORの意味。
    dp[i] |= set('(' + S + ')' for S in dp[i - 2])
    # print("before dp[i]:",i,dp[i])

    for l in range(2, i, 2):
        r = i - l
        dp[i] |= set(SL + SR for SL in dp[l] for SR in dp[r])

    # print("after dp[i]:",i,dp[i])

ANS = sorted(dp[n])

print(*ANS, sep='\n')
