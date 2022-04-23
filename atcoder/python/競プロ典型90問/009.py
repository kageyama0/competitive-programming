# https://atcoder.jp/contests/typical90/tasks/typical90_i
# ある点を原点として固定する。
# TODO: 途中。反対の角度から一番近いやつをどうやって見つけるか悩み中


from math import atan2, degrees
import bisect


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]


# i: 原点とする点のインデックス
ans = 0
for i in range(N):
    origin_x, origin_y = XY[i][0], XY[i][1]
    angles = []
    for j in range(N):
        if i == j:
            continue

        x, y = XY[j][0]-origin_x, XY[j][1]-origin_y
        angle = degrees(atan2(y, x))
        if 0 <= angle <= 180:
            angles.append(angle)
        elif -180 <= angle < 0:
            angles.append(360+angle)
        # print("i", i, "j", j, "angle", angle)

    angles.sort()
    print("angles", angles)

    angles_cnt = N-1
    for j in range(angles_cnt):
        angle = angles[j]
        ideal_angle = angle + 180 if 0 <= angle <= 180 else angle - 180
        idx = bisect.bisect_left(angles, ideal_angle)
