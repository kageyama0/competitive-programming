# https://atcoder.jp/contests/abc268/tasks/abc268_d
import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

S = [input().rstrip() for _ in range(n)]
T = {input().rstrip() for _ in range(m)}
# print(S, T)
available = 16 - sum(map(len, S)) - n + 1

if n == 1:
    for s in S:
        if s not in T and len(s) >= 3:
            print(s)
            exit()
    print(-1)
    exit()

for p_s in permutations(S):
    q = deque()
    q.append((p_s[0], 1, available))
    while q:
        s, i, available = q.pop()
        if i == n:
            if s not in T:
                print(s)
                exit()
            continue

        for j in range(available + 1):
            q.append((s + "_" * (j+1) + p_s[i], i+1, available - j))

print(-1)
