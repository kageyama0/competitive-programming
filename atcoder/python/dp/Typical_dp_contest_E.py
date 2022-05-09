MOD = 10 ** 9 + 7
D = int(input())
N = input()
length = len(N)

# dp[i][flag_smaller][mod_d] := i桁目までの数字について、flag_smallerが未満フラグ、mod_dがDで割った余りの数
dp = [[[0]*D for _ in range(2)] for _ in range(length+1)]
dp[0][0][0] = 1
# print(dp)

for i in range(length):
    max_digit = int(N[i])

    # 未満フラグが立っているかものとそうでないもので処理を変える
    for flag_smaller in [0, 1]:
        digit_range = 9 if flag_smaller else max_digit

        # それまでの余りによって処理を変える
        for mod_d in range(D):

            # この桁で使う数字dによって処理を変える
            for d in range(digit_range+1):
                flag_smaller_next = 1 if flag_smaller else 0

                if d < max_digit:
                    flag_smaller_next = 1

                mod_d_next = (mod_d + d) % D
                dp[i+1][flag_smaller_next][mod_d_next] += dp[i][flag_smaller][mod_d] % MOD
                # print("前", i, flag_smaller, mod_d,"後", i+1, flag_smaller_next, mod_d_next,)
                # print(dp)



print((dp[length][0][0] + dp[length][1][0] - 1) % MOD)
