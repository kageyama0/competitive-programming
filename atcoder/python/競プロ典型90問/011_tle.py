# https://atcoder.jp/contests/typical90/tasks/typical90_k

# 締め切りが早い順にタスクをこなすことが最良
# また早い順で全部のタスクをこなしていく訳でなく、そのタスクをやるかやらないかの選択もする
# ただし、これだとTLEになる

from collections import deque

n = int(input())
jobs = []
for _ in range(n):
    limit_day, cost_day, salary = map(int, input().split())
    if limit_day >= cost_day:
        jobs.append([limit_day, cost_day, salary])

jobs.sort(key=lambda x: x[0])
# print(jobs)

ans = 0
q = deque()
# やるかどうか迷っている仕事、使っている日数、もらっている給料をqに入れる
q.append([0, 0, 0])
while q:
    idx, day, salary = q.popleft()
    if idx == len(jobs):
        ans = max(ans, salary)
        continue

    # その仕事をやらない場合
    q.append([idx+1, day, salary])

    # その仕事をやる場合
    if day + jobs[idx][1] <= jobs[idx][0]:
        q.append([idx+1, day+jobs[idx][1], salary+jobs[idx][2]])

print(ans)
