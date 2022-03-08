# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
N = int(input())
P = list(map(int, input().split()))
scores = set([0])
for p in P:
    for s in list(scores):
        scores.add(s+p)
print(len(scores))
