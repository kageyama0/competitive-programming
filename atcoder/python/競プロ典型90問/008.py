# https://atcoder.jp/contests/typical90/tasks/typical90_h

# https://twitter.com/e869120/status/1379927227739987972/photo/1
# どうやら、状態DPなるものを実装する必要があるらしい
# https://drken1215.hatenablog.com/entry/2022/04/01/121700


# a に b を足して MOD をとる関数
def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    return a


N = int(input())
S = input()

MOD = 10**9+7
T = 'atcoder'


# DP テーブル
dp = [[0]*(len(T)+1) for _ in range(N+1)]

# 初期条件,
dp[0][0] = 1

for i in range(N):
    for j in range(len(T)+1):
        # S[i] を選ばない場合
        dp[i+1][j] = add(dp[i+1][j], dp[i][j])

        # S[i] を選ぶ場合
        if j < len(T) and S[i] == T[j]:
            dp[i+1][j+1] = add(dp[i+1][j+1], dp[i][j])

print(*dp, sep="\n")
print(dp[N][len(T)])
