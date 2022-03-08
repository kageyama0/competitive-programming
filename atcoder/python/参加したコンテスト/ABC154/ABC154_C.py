import numpy as np

n = int(input())
A = np.array(list(map(int, input().split())))

B = np.unique(A)

if n == len(B):
    print("YES")
else:
    print("NO")
