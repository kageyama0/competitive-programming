# https://atcoder.jp/contests/typical90/tasks/typical90_j
from itertools import accumulate

N = int(input())

S = [[0]*(N+1) for _ in range(2)]
for i in range(N):
    C, P = map(int, input().split())
    S[C-1][i+1] = P

# print(S)
S = [list(accumulate(S[0])), list(accumulate(S[1]))]
# print(S)


Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(S[0][R] - S[0][L-1], S[1][R] - S[1][L-1])
