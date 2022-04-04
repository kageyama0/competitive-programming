x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


d_x = dict()
for x in [x1, x2, x3]:
    if d_x.get(x) is None:
        d_x[x] = 1
    else:
        d_x[x] += 1

d_y = dict()
for y in [y1, y2, y3]:
    if d_y.get(y) is None:
        d_y[y] = 1
    else:
        d_y[y] += 1

# print(d_x, d_y)

for x in d_x.keys():
    if d_x[x] == 1:
        ans_x = x

for y in d_y.keys():
    if d_y[y] == 1:
        ans_y = y

print(ans_x, ans_y)
