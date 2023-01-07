h, w = map(int, input().split())

maze = [["-"] * (w + 2) for _ in range(h + 2)]
for i in range(h):
    line = list(input())
    maze += ["-" + line + "-"]
    if "s" in line:
        s_x, s_y = line.index("s"), i
    if "g" in line:
        g_x, g_y = line.index("g"), i
maze.append(["-"] * (w + 2))

dist = [[float("inf")] * (w + 2) for _ in range(h + 2)]

q = [(s_x, s_y, 0)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
    next_q = []
    for x, y in q:
        for dx, dy in dir:
            next_x, next_y = x + dx, y + dy

    q = next_q

print(maze)
