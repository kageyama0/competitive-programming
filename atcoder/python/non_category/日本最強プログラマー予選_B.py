import numpy as np


def main():
    n, k = map(int, input().split())
    A = np.array(list(map(int, input().split())))
    MOD = 10 ** 9 + 7
    #転倒数、Aの中で
    C1 = np.array([0] * n)
    C2 = np.array([0] * n)
    for i in range(n):
        C1[i] = np.count_nonzero(A[i:] < A[i])
        C2[i] = np.count_nonzero(A < A[i])
    c1, c2 = C1.sum(), C2.sum()
    ans = 0

    ans += c1 * k % MOD
    ans += c2 * (k * (k - 1) // 2 % MOD)

    print(ans % MOD)


if __name__ == "__main__":
    main()
