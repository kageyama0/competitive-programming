#

from collections import deque

h, w = map(int, input().split())

graph = [[] for _ in range(h)]
for i in range(h):
    C = list(input())
    graph[i] = C

    if "S" in C:
        s_y, s_x = i, C.index("S")

q = deque()
q.append((s_y, s_x, None, None))
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()
while q:
    y, x, prev_y, prev_x = q.pop()
    visited.add((y, x))

    # 上下左右に動いてみる
    for dy, dx in dir:
        next_y, next_x = y + dy, x + dx
        if 0 <= next_y < h and 0 <= next_x < w:
            # 障害物に当たるか、前の場所に戻る場合はスキップ
            if graph[next_y][next_x] == "#" or (next_y, next_x) == (prev_y, prev_x):
                continue

            # Sにたどり着いた場合
            if graph[next_y][next_x] == "S":
                print("Yes")
                exit()

            # すでに訪れた場所の場合はスキップ。Sがすでに訪れた場所なので、上の処理の後にこれを書く
            if (next_y, next_x) in visited:
                continue

            # 道があった場合
            q.append((next_y, next_x, y, x))

print("No")
