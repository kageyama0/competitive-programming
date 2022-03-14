# https://atcoder.jp/contests/tdpc/tasks/tdpc_number
# よくわからん...

mod = 10**9+7
# d = int(input())
# n = input()
d = 4
n = "16"

# 全ての数は 0 ~ d-1 (mod d)なので、長さdの配列でオッケー
dp = [0]*d

tmp = 0
for i in n:

    dp2 = [0]*d
    dp, dp2 = dp2, dp
    print("dp,dp2:",dp, dp2)

    for j in range(d):
        for k in range(10):
            print(j,k,dp[(j+k) % d],dp2[j])
            dp[(j+k) % d] += dp2[j]
            dp[(j+k) % d] %= mod

        print("dp:",dp)

    for j in range(int(i)):
        dp[(tmp+j) % d] += 1

    tmp += int(i)
    print(dp)

if tmp % d != 0:
    dp[0] -= 1

print(dp[0] % mod)
