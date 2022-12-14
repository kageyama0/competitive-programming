N = int(input())
T = input()

dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
now_dir = 0
now_x, now_y = 0, 0
for i in range(N):
    st = T[i]

    if st == "S":
        plus_x, plus_y = dir[now_dir][0], dir[now_dir][1]
        now_x += plus_x
        now_y += plus_y

    if st == "R":
        now_dir = (now_dir + 1) % 4

print(now_x, now_y)
