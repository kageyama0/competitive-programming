import sys
from collections import deque

buf = sys.stdin.buffer

h, w = map(int, buf.readline().split())
map = ""
for _ in range(h):
    map += input() + "#"
# print(map)

n = h * (w + 1)
periods = [[] for _ in range(n)]
dir = [-w - 1, 1, -1, w + 1]
for i in range(n):
    if map[i] == "#":
        continue
    for d in dir:
        next_i = i + d
        if next_i < 0 or next_i >= n or map[next_i] == "#":
            continue
        periods[i].append(next_i)
# print(periods)

q = deque()


def bfs(now_i):
    for next_i in periods[now_i]:
        if con_cnt[next_i] == -1:
            con_cnt[next_i] = con_cnt[now_i] + 1
            q.append(next_i)
    # まだスタックが残っている場合、左から抜き出す
    if q:
        bfs(q.popleft())


start_points = [i for i, j in enumerate(periods) if len(j) > 0]
ans = 0
for start_point in start_points:
    con_cnt = [-1] * n
    con_cnt[start_point] = 0
    bfs(start_point)
    print(con_cnt)
    ans = max(ans, max(con_cnt))

print(ans)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# https://atcoder.jp/contests/abc151/submissions/9710366
# from collections import deque
# import sys
# buf = sys.stdin.buffer

# h, w = map(int, buf.readline().split())
# maze = ''
# # グラフのしきりとして"#"をつける
# for _ in range(h):
#     maze += input() + '#'

# n = h * (w + 1)
# graph = [[] for _ in range(n)]
# dir = [-w - 1, -1, 1, w + 1]
# for i in range(n):
#     if maze[i] == '#':
#         continue
#     for j in dir:
#         ind = i + j
#         if ind < 0 or n <= ind or maze[ind] == '#':
#             continue
#         # 隣り合っている . のインデックスを記録する
#         graph[i].append(ind)

# que = deque()
# def BFS(node):
#     for i in graph[node]:
#         if lengths[i] < 0:
#             lengths[i] = lengths[node] + 1
#             que.append(i)
#     if len(que) > 0:
#         BFS(que.popleft())

# # graphに記録した"#"でない部分、つまり[]になっていないやつ、つまりlen() > 0のとこだけ
# starts = [i for i, j in enumerate(graph) if len(j) > 0]
# max_len = 0
# for start in starts:
#     lengths = [-1] * n
#     lengths[start] = 0
#     BFS(start)
#     max_len = max(max_len, max(lengths))
# print(max_len)


# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# from collections import deque
# import copy

# def bfs(start, s):
#     h = len(s)
#     w = len(s[0])
#     distance = 0
#     maze = [[-1] * w for _ in range(h)]
#     maze[start[0]][start[1]] = 0
#     s[start[0]][start[1]] = "#"
#     drcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     q = deque()
#     q.append(start)
#     while(q):
#         cr, cc = q.popleft()
#         for dr, dc in drcs:
#             nr, nc = cr + dr, cc + dc
#             if nr < 0 or nc < 0 or nr >= h or nc >= w:
#                 continue
#             if s[nr][nc] == ".":
#                 q.append([nr, nc])
#                 s[nr][nc] = "#"
#                 maze[nr][nc] = maze[cr][cc] + 1
#                 if maze[nr][nc] > distance:
#                     distance = maze[nr][nc]
#                     goal = [nr, nc]
#     return goal, distance

# def main():
#     h, w = map(int, input().split())
#     s = [list(input()) for _ in range(h)]
#     for r in range(h):
#         if "." in s[r]:
#             start = [r, s[r].index(".")]
#     goal, distance = bfs(start, copy.deepcopy(s))
#     _, res = bfs(goal, s)
#     print(res)

# if __name__ == '__main__':
#     main()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# h,w = map(int,input().split())
# edge = ["#"] * (w + 2)
# map = [edge]
# sx, sy = 0, 0
# for i in range(1, h + 1):
#     line = input()
#     map.append(list("#" + line + "#"))
#     if not sx:
#         sx = i
#         sy = line.index(".")
# map.append(edge)

# s = deque()
# s.append((sx, sy))
# dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# while s:
#     stack_x, stack_y = s.pop()
#     for dx, dy in dxy:
#         next_x, next_y = stack_x + dx, stack_y + dy
#         if map[next_x][next_y] == ".":
