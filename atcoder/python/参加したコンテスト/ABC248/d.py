# 範囲を検索するのに二分探索を使う。
# L以上R以下で当てはまるものの数を探す ＝ L,Rの入る位置の差を求める

from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

B = [[] for _ in range(N+1)]
for i, a in enumerate(A):
    B[a].append(i)
print(B)

for _ in range(Q):
    L, R, X = map(int, input().split())
    Li = bisect_left(B[X], L-1)
    Ri = bisect_right(B[X], R-1)
    print("X:", X, "L:", L, "R:", R, "Li:", Li, "Ri:", Ri)
    print(Ri-Li)
