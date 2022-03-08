# 累積和
import numpy as np
from numba import njit

@njit(cache=True)
def loop(n, k, A):
    for _ in [0] * k:
        B = np.zeros(n + 1, dtype=np.int64)
        for i in range(n):
            left = max(0, i - A[i])
            right = min(n, i + A[i] + 1)
            B[left] += 1
            B[right] -= 1
        A = np.cumsum(B)[:-1]
        print(A)
        if np.all(A == n):
            return A
            break

    return A


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    A = np.array(a, dtype=np.int64)
    A = loop(n, k, A)
    print(*A)


if __name__ == "__main__":
    main()
