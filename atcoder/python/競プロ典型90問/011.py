# https://atcoder.jp/contests/typical90/tasks/typical90_k

N = int(input())
DCS = []
max_d = 0
for _ in range(N):
    D, C, S = map(int, input().split())
    DCS.append([D, C, S])
    max_d = max(max_d, D)

dp = [[0]*max_d for _ in range(N+1)]
print(dp)
DCS = sorted(DCS, key=lambda x: x[0])

for x in range(N):
    d, c, s = DCS[x]
    for i in range(N+1):
        for j in range(max_d):
            if j < c or j > d:
                continue

            
