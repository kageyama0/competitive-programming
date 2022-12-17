# 方針
# 辞書順で小さいものを１から計算する必要はない？
# (バラバラ) | (小さい順に並んでいるところ) のところで区切れて
# バラバラの最後尾とその数字より小さいやつを入れ替える
# その後、小さい順に並んでいるところを逆順にする

n = int(input())
P = list(map(int, input().split()))

# バラバラの最後尾を見つける
last_idx = 0
for i in range(n-1, 0, -1):
    if P[i-1] > P[i]:
        last_idx = i - 1
        break

# バラバラの最後尾より小さいやつの中でできるだけ大きいやつと入れ替える
target = last_idx + 1
for i in range(last_idx, n):
    if P[last_idx] > P[i]:
        target = i
P[last_idx], P[target] = P[target], P[last_idx]
ans = P[:last_idx+1] + P[last_idx+1:][::-1]
print(*ans)
