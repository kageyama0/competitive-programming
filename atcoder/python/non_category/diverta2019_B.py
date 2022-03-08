from itertools import combinations
from collections import Counter


def main():
    n = int(input())
    if n == 1:
        print(1)
        exit()

    XY = [list(map(int, input().split())) for _ in range(n)]
    d = []
    for A, B in combinations(XY, 2):
        x1, y1 = A[0], A[1]
        x2, y2 = B[0], B[1]
        p, q = x2 - x1, y2 - y1
        d.append((p, q))
        d.append((-p, -q))
    # print(d)
    # print(Counter(d))

    C = Counter(d)
    ans = 0
    for v in C.values():
        ans = max(ans, v)
    print(n - ans)


if __name__ == "__main__":
    main()
