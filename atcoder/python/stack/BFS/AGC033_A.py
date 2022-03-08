import sys
input = sys.stdin.readline

h, w = map(int, input().split())
M = []
q = []
for i in range(h):
    line = input().strip()
    M.append(list(line))
    for j in range(w):
        if line[j] == "#":
            M[i][j] = 0
            q.append((j, i))

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
cnt = 0
while q:
    next_q = []
    cnt += 1
    for x, y in q:
        for dx,dy in dir:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_y <= h - 1 and 0 <= next_x <= w - 1:
                if M[next_y][next_x] == ".":
                    M[next_y][next_x] = M[y][x] + 1
                    q.append((next_x, next_y))
    q = next_q

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, M[i][j])
print(ans)
