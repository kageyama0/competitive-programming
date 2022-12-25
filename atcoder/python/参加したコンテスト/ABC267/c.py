# https://atcoder.jp/contests/abc267/tasks/abc267_c

# 数列
# 連続部分列の最大値を求める
# 例えば、以下のような和の式があるとする
# S1(5) = 1 * A1 + 2 * A2 + 3 * A3 + 4 * A4 + 5 * A5
# S1(2) = 1 * A1 + 2 * A2
# S2 = A3 + A4 + A5

# これを操作すると
# S1(5) - S1(2)          = 3 * A3 + 4 * A4 + 5 * A5
# S1(5) - S1(2) - 2 * S2 = 1 * A3 + 2 * A4 + 3 * A5 (こういうのがが求めたいもの)

# つまり、S1のような和とS2のような和を求めておいて、あとで計算すれば良い

n, m = map(int, input().split())
a = list(map(int, input().split()))
s1 = [0] * (n + 1)
s2 = [0] * (n + 1)
for i in range(n):
    s1[i+1] = s1[i] + i * a[i]
    s2[i+1] = s2[i] + a[i]

# print(s1, s2)


ans = -10 ** 18
for i in range(n - m + 1):
    ans = max(ans, s1[i+m] - s1[i] - (i - 1) * (s2[i+m] - s2[i]))
print(ans)
