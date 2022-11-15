# 方針: 各々のコマの位置がどこかを記録して、その縦横の差を計算する

h, w = map(int, input().split())
o_list = []

for i in range(h):
    s = list(input())
    for j in range(w):
        if s[j] == "o":
            o_list.append((i, j))

o1_h, o1_w = o_list[0][0], o_list[0][1]
o2_h, o2_w = o_list[1][0], o_list[1][1]

ans = sum([abs(o1_h - o2_h), abs(o1_w - o2_w)])
print(ans)
