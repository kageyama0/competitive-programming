# https://atcoder.jp/contests/abc029/tasks/abc029_c
# itertools.product()
from itertools import product
n = int(input())
ans = list(product(["a", "b", "c"], repeat=n))
for a in ans:
    print("".join(a))
