# numpyのdtypeについて
# https://github.com/lesguillemets/notes/blob/master/2013/Nov/28.np.dtype.md

import numpy as np
# -------------- array, concatenate ---------------
a = np.array(0, 6)                  # [0,1,2,3,4,5]
b = np.array(6, 10)                 # [6,7,8,9]
concat_ab = np.concatenate([a, b])  # [0,1,2,3,4,5,6,7,8,9]

# -------------- arrange ---------------
print(np.arange(3))
# [0 1 2]

print(np.arange(3, 10))
# [3 4 5 6 7 8 9]

print(np.arange(3, 10, 2))
# [3 5 7 9]

print(np.arange(0.3, 1.0, 0.2))
# [0.3 0.5 0.7 0.9]

print(np.arange(-3, 3))
# [-3 -2 -1  0  1  2]

print(np.arange(10, 3))
# []

print(np.arange(10, 3, -2))
# [10  8  6  4]


# -------------- reshape ---------------
np.reshape(a,(2,3)) #[[0,1,2][3,4,5]]
np.reshape(a, (2, -1)) #-1は、計算して勝手に３として整形してくれる

# -------------- maximum ---------------
x = [10, 20, 30]
y = [20, 15, 10]
m = np.maximum(x, y)
# numpy.maximum()の戻り値を格納する配列を指定します。これを指定する場合は、アウトプット先の配列と戻り値の配列のshapeが一致している必要があります。

m1 = numpy.maximum.accumulate(numpy.array([11, 12, 13, 20, 19, 18, 17, 18, 23, 21]))
# m1 = array([11, 12, 13, 20, 20, 20, 20, 20, 23, 23])

# -------------- .frombuffer(buffer, dtype, count, offset) ---------------
# この関数は、引数bufferとして渡されたbufferを１次元配列に変換するものです。countやoffsetでデータを読み込む個数や開始点を指定できます。また、dtypeで返される配列のデータ型を指定することができます。
# この関数を使うことでndarrayへの高速化が期待できるので、大容量のデータを扱う方にはおすすめです。
grid = np.frombuffer(read(), 'S1').reshape(H, -1)[:, :W]

# -------------- where -------------------------------
print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(np.where(a < 4, -1, 100))
# [[ -1  -1  -1]
#  [ -1 100 100]
#  [100 100 100]]

print(np.where((a > 2) & (a < 6), -1, 100))
# [[100 100 100]
#  [ -1  -1  -1]
#  [100 100 100]]

print(np.where((a > 2) & (a < 6) | (a == 7), -1, 100))
# [[100 100 100]
#  [ -1  -1  -1]
#  [100  -1 100]]

print(np.where(a < 4, -1, a))
# [[-1 -1 -1]
#  [-1  4  5]
#  [ 6  7  8]]

print(np.where(a < 4, a, 100))
# [[  0   1   2]
#  [  3 100 100]
#  [100 100 100]]

# -------------- dtype,astype -----------------
print(a.dtype)
# [1 2 3]
# int64
a_float = a.astype(np.float32)

# -------------- cross -----------------
# ベクトルu,vを定義
u = [3, 1, 0]
v = [2, 5, 1]

# uとvのベクトル積w
w = np.cross(u, v)

# -------------- cumsum(累積和)、diff(差分) ------------------
# https://qiita.com/Sa_qiita/items/fc61f776cef657242e69
a = np.array([1, 2, 3, 4, 5, 6])
np.cumsum(a)
>> > array([1, 3, 6, 10, 15, 21])

In[2]: a = np.array([1, 2, 4, 1, 6, 8, 3])  # 適当に値を並べた配列を用意する

In[3]: np.diff(a, n=1)  # まずはn=1から。
array([1,  2, -3,  5,  2, -5])

# -------------- dtype -------------------------------
# https://github.com/lesguillemets/notes/blob/master/2013/Nov/28.np.dtype.md
# a[1 2 3] int64
# b[1.  2.] float64
# c[True False] bool
# d[] float64
# e['t' 'h' 'e'] | S1
# f['there'] | S5
# g[0.  0.] float64
# h[6.90542876e-310   1.61356702e-316] float64
# i[0 0] int64
# j[0 0] int8
# k[0 0] int8


# -------------- binary search(二分探索) ------------------
# https://wa3.i-3-i.info/word1614.html
# A = np.array([1,3,7,9])

np.searchsorted([1,2,3,4,5], 3)
2
np.searchsorted([1,2,3,4,5], 3, side='right')
3
np.searchsorted([1,2,3,4,5], [-10, 10, 2, 3])
array([0, 5, 1, 2])
