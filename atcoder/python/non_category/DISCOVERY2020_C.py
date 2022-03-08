# いちごを切り分けるやつ
# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c

import numpy as np
import sys
h, w, k = map(int, input().split())

ans = [[0] * w for _ in range(h)]

berry = 1
for i in range(h):
  line = list(input())
  for j, st in enumerate(line):
    if st == "#":
      ans[i][j] = berry
      berry += 1

for i in range(h):
  for j in range(1,w):
    if ans[i][j] == 0:
      ans[i][j] = ans[i][j - 1]

for i in range(h):
  for j in range(w-1)[::-1]:
    if ans[i][j] == 0:
      ans[i][j] = ans[i][j+1]

for a in ans:
  print("".join(map(str, a)))


#----------maspy-------------
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines


# H, W, K = map(int, readline().split())

# bufferとして読み込む。H行とそれに合う横列の数を計算して整形。[:,:w]で改行コードを消す
# grid = np.frombuffer(read(), 'S1').reshape(H, -1)[:, :W]

# ”＃”がある場所のインデックスを記録
# X, Y = np.where(grid == b'#')

# A = np.zeros((H, W), np.int32)
# A[X, Y] = np.arange(1, K+1)

# 累積和ではなく、その地点までの最大値を持っといて最大値にしていく累積最大値とでもいうのか。
# np.maximum.accumulate(A, axis=1, out=A)

# for w in range(W-2, -1, -1):
# w列目が0なら、(w+1)列めの値と真偽値１をかけてそれにする
#     A[:, w] += A[:, w+1] * (A[:, w] == 0)

# for h in range(1, H):
#     if A[h, -1] == 0:
#         A[h] += A[h-1]
# for h in range(H-1, -1, -1):
#     if A[h, -1] == 0:
#         A[h] += A[h+1]


# print('\n'.join(' '.join(row) for row in A.astype(str)))
