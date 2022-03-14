# https://atcoder.jp/contests/abc007/tasks/abc007_4
# https://torus711.hatenablog.com/entry/20150423/1429794075
# https://yottagin.com/?p=7249

# ０以上N以下の整数の内、4or9を含めた数字の個数を返す関数
def f(N):
    length = len(N)
    # dp[ 桁数 ][ 未満フラグ ][4 or 9] := 総数
    dp = [[[0]*2 for _ in range(2)] for _ in range(length+1)]

    dp[0][0][0] = 1
    for i in range(length):
        # i桁目に使える数字の最大値 max_digit
        max_digit = int(N[i])

        # 未満フラグ 1 or 0
        for flag_less in [0, 1]:

            # 4 or 9使ってるかフラグ
            for flag_four_or_nine in [0, 1]:

                # 前の桁で
                range_digit = 9 if flag_less else max_digit
                for d in range(range_digit+1):
                    flag_less_next = 0
                    flag_four_or_nine_next = 0

                    if flag_less == 1 or d < max_digit:
                        flag_less_next = 1

                    if flag_four_or_nine == 1 or d == 4 or d == 9:
                        flag_four_or_nine_next = 1
                        
                    dp[i+1][flag_less_next][flag_four_or_nine_next] += dp[i][flag_less][flag_four_or_nine]

    # print(dp)

    return dp[length][0][1]+dp[length][1][1]


a, b = input().split()
ans = f(b) - f(str(int(a)-1))
print(ans)
