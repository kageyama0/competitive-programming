from collections import deque

H, W = map(int, input().split())
edges = ['#'] * (W + 2)
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
field = [edges]
# スタート位置の記録と図の作成
for i in range(H):
    line = input()
    field.append(['#'] + list(line) + ['#'])
    if 's' in line:
        sx, sy = i+1, line.index('s')+1
field.append(edges)

s = deque()
push, pop = s.append, s.pop
push((sx, sy))
while s:
    cx, cy = pop()
    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        if field[nx][ny] == '#':
            continue
        if field[nx][ny] == 'g':
            print('Yes')
            exit()
        push((nx, ny))
        field[nx][ny] = '#'
print('No')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# h, w = map(int, input().split())
# edge = ["#"] * (w + 2)
# map = [edge]
# for i in range(1, h + 1):
#     line = input()
#     map.append(list("#" + line + "#"))
#     if "s" in line:
#         # ここに注意！sx,syを逆に書くミスをしがち
#         sx = i
#         sy = line.index("s") + 1
# map.append(edge)

# stack = deque()
# stack.append((sx, sy))
# d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# while stack:
#     stack_x, stack_y = stack.pop()
#     for dx, dy in d:
#         next_x = stack_x + dx
#         next_y = stack_y + dy
#         if map[next_x][next_y] == "g":
#             print("Yes")
#             exit()
#         if map[next_x][next_y] == "#":
#             continue
#         stack.append((next_x, next_y))
#         map[next_x][next_y] = "#"
#     # print(stack)
# print("No")
