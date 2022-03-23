# 場合の数
# 累積和を使えばできそう？ => TLE
# 解説を読むと、どうやら最小値と最大値が求まれば、それ間の数は全て可能解らしい
# 最大値 = (元の配列の連続部分配列の0の数-1の数)の最大値
# 最小値 = (元の配列の連続部分配列の0の数-1の数)の最小値


N = int(input())
A = list(map(int, input().split()))

#
min_count = 0
max_count = 0
m = 0
M = 0

for i in range(N):
    if A[i] == 1:
        m = min(m-1, -1)
        M = max(M-1, 0)
    else:
        m = min(m+1, 0)
        M = max(M+1, 1)

    min_count = min(min_count, m)
    max_count = max(max_count, M)

    # print(min_count, max_count)

print(max_count-min_count+1)
