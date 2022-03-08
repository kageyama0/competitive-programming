import numpy as np
import sys
buf = sys.stdin.buffer

h,w = map(int,buf.readline().split())
grid = np.array([list(input()) for _ in range(h)])
grid = np.where(grid == ".", 1, 0)
#print(grid)

L, R, U, D = [np.zeros((h, w)) for _ in range(4)]
for i in range(w):
    L[:, i] = (L[:, i - 1] + 1) * grid[:, i]
    R[:, -i - 1] = (R[:, -i] + 1) * grid[:, -i - 1]

for i in range(h):
    D[i,:] = (D[i - 1,:] + 1) * grid[i,:]
    U[-i - 1,:] = (U[-i,:] + 1) * grid[-i - 1,:]

print(int(np.max(L + R + D + U) - 3))


# # maspy https://atcoder.jp/contests/abc129/submissions/5884497
# import numpy as np
# import sys
# buf = sys.stdin.buffer

# H,W = map(int,buf.readline().split())
# # 周りに壁を、0,1化、壁を0で持つ
# grid = np.zeros((H+2,W+2),dtype=np.bool)
# grid[1:-1,1:] = (np.frombuffer(buf.read(H*(W+1)),dtype='S1') == b'.').reshape((H,W+1))

# # x軸方向の集計
# def F(transpose):
#   x = grid
#   if transpose:
#     x = (x.T).copy()
#   x = np.ravel(x) # to 1D array
#   L = len(x)

#   left_zero = -np.arange(L) # 左の壁のindexの-1倍
#   left_zero[x] = 0
#   np.minimum.accumulate(left_zero, out=left_zero)

#   right_zero = np.arange(L) # 逆順ソートした上で左の壁のindex
#   right_zero[x[::-1]] = 0
#   np.maximum.accumulate(right_zero, out=right_zero)

#   y = left_zero
#   y += L-right_zero[::-1]

#   return y.reshape(grid.T.shape).T if transpose else y.reshape(grid.shape)

# answer = (F(False) + F(True)).max()-5
# print(answer)
