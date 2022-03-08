import numpy as np


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    A = np.array(a)
    limit = 10 ** 18

    if A[-1] == 0:
        print(0)
    elif A[0] > limit:
        print(-1)
    else:
        ans = A[0]
        for i in range(1, n):
            ans *= A[i]
            if ans > limit:
                print(-1)
                exit()

        print(ans)


if __name__ == "__main__":
    main()
