# 愚直に組み合わせを求めて、それぞれの和を求めて、それがdの倍数になるかどうかを計算すると絶対にTLEになるよなー
# 最大値を求められれば良いので、ソートしてうまくやれないか？
# => 結果、TLEどころかWAもちらほら...数字がデカすぎるのかな？
# MODとるか
from itertools import combinations

n, k, d = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
comb = list(combinations(range(n), k))
for c in comb:
    ans = 0
    for i in c:
        ans += A[i]
    if ans % d == 0:
        print(ans)
        exit()

print(-1)
