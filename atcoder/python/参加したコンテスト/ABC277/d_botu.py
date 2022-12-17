# 愚直にやったらどうなる？
# => TLE
# 何に時間がかかるのか？
# 全探索せずに、始める地点を決める
from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))
d = dict(Counter(A))
# print(c)

s = sum(k * v for k, v in d.items())

ans = n * m
for k, v in d.items():
    now = k
    cnt = 0
    # nowに一致するカードを消費して、+1したカードがあればそのカードを消費して、を繰り返す
    while now in d:
        cnt += now * d[now]
        now += 1

    # 消費したカードの合計を引いた値が最小値であれば更新
    ans = min(ans, s-cnt)

print(ans)
