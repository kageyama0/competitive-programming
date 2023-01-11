# https://atcoder.jp/contests/abc270/tasks/abc270_d
# 石取りゲーム
# 貪欲法？ => 「二人とも」取り除いた石の個数を最大化しないといけない、だった

n, k = map(int, input().split())
A = list(map(int, input().split()))

# dp[i]: 石が i 個残っている状態からゲームを始めたとき、先手が取ることのできる石の個数
dp = [0] * (n + 1)

for i in range(n+1):
    for j in range(k):
        if A[j] > i:
            break

        dp[i] = max(dp[i], i - dp[i - A[j]])

print(dp[n])
