# E:溶解度、F：砂糖＋水の合計重量の限界
A,B,C,D,E,F = map(int,input().split())
W = []
S = []

# 100A,100B の水
max_a = F // (100 * A )
for a in range(max_a + 1):
    max_b = (F - 100 * a) // (100 * B)
    for b in range(max_b + 1):
        water = 100 * (a * A + b * B)
        if 0 < water <= F:
            W.append(water)

# c,d の砂糖
for c in range(1 + F // C):
    for d in range(1 + F // D):
        sugar = c * C + d * D
        if sugar <= F:
            S.append(sugar)

W = list(set(W))
S = list(set(S))

# x = -1 にしておかないと、溶解度が０のやつしか出来ない時、REになる。
x = -1
for w in W:
    for s in S:
        if w + s <= F:
            sol = 100 * s / w
            if x < sol <= E:
                x = sol
                X, Y = w + s, s

print(X,Y)
