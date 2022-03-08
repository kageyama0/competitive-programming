n = int(input())
s = list(input())
r_pos = []
g_pos = []
b_pos = []

for i in range(n):
    st = s[i]
    if st == "R":
        r_pos.append(i)

    if st == "G":
        g_pos.append(i)

    if st == "B":
        b_pos.append(i)

colors = [r_pos, g_pos, b_pos]
if len(colors[0]) > len(colors[1]):
    colors[0], colors[1] = colors[1], colors[0]
if len(colors[0]) > len(colors[2]):
    colors[0], colors[2] = colors[2], colors[0]
if len(colors[1]) > len(colors[2]):
    colors[1], colors[2] = colors[2], colors[1]

x_num, y_num, z_num = len(colors[0]), len(colors[1]), len(colors[2])

ans = x_num * y_num * z_num
c = set(colors[2])
for a in colors[0]:
    for b in colors[1]:
        x, y = min(a, b), max(a, b)

        dif = y - x
        left_pos = x - dif
        right_pos = y + dif
        mid_pos = 4000
        if dif % 2 == 0:
            mid_pos = x + dif // 2

        left = 0
        right = 0
        mid = 0
        if left_pos in c:
            left = 1
        if right_pos in c:
            right = 1
        if mid_pos in c:
            mid = 1

        ans -= left + right + mid

print(ans)
