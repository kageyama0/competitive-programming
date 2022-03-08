from collections import defaultdict
import numpy as np


def main():
    n = int(input())
    s = list(input())
    num_idx = [[] for _ in range(10)]
    for i in range(n):
        num_idx[int(s[i])].append(i)

    I = np.array(num_idx)

    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                try:
                    x = np.amin(I[i])
                    J = I[j]
                    J = J[J > x]
                    y = np.amin(J)
                    K = I[k]
                    K = K[K > y]
                    z = np.amin(K)
                    print(x, y, z)
                except ValueError:
                    continue

                if x < y < z:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
