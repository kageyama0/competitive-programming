import sys
input = sys.stdin.readline

h, w = map(int, input().split())
maze = [list("#" * (w + 2))]
white = 0
for _ in [0] * h:
    line = "#" + input().strip() + "#"
    maze.append(list(line))
    white += line.count(".")
maze += [list("#" * (w + 2))]
maze[1][1] = 0
maze[-2][-2] = "goal"

q = set([(1, 1)])
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dis = 0
while q:
    next_q = set()
    dis += 1
    for x, y in q:
        print("x,y:", x, y)

        maze[y][x] = dis

        for dx, dy in dir:
            next_x, next_y = x + dx, y + dy
            if maze[next_y][next_x] == ".":
                print(next_y,next_x)
                next_q.add((next_y, next_x))

            if maze[next_y][next_x] == "goal":
                print(white - dis - 1)
                exit()
    q = next_q
print(-1)
