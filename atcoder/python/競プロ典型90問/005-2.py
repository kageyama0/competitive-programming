n, b, k = map(int, input().split())
C = list(map(int, input().split()))
MOD = 10 ** 9 + 7
dp = [[0] * (b) for _ in range(n+1)]

for i in range(1, n+1):
    # N桁の整数が対象ってことは、1桁目は0が含まれない
    # print(i, dp)
    if i == 1:
        for j in C:
            dp[i][j % b] += 1
    else:
        # jはi桁目に使う数字
        for j in C:
            # kはi-1桁の数字(mod b)
            for k in range(b):
                remainder = (10 * k + j) % b
                # print("i-1桁の数字(mod b):", k, "この桁で使う数字:", j, "余り", remainder)

                # print(dp[i-1][k])
                dp[i][remainder] += dp[i-1][k]

# print(dp)
print(dp[-1][0] % MOD)
