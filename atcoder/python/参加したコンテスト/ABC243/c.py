n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
s = input()

right_people, left_people = dict(), dict()
for i in range(n):
    dir = s[i]
    x_pos, y_pos = xy[i][0], xy[i][1]

    # i番目の人間iさんが右を向いている時
    if dir == "R":
        # iさんと同じY座標上にいて左を向いている人間が存在する
        if y_pos in left_people:
            # その人の座標がiさんよりも右である
            if x_pos < left_people[y_pos]:
                print("Yes")
                exit()

        # iさんと同じY座標にいて、同じように右を向いている人間がいる場合
        if y_pos in right_people:
            right_people[y_pos] = min(x_pos, right_people[y_pos])
        else:
            right_people[y_pos] = x_pos

    # i番目の人間が左を向いている時
    else:
        # iさんと同じY座標上にいて右を向いている人間が存在する
        if y_pos in right_people:
            # その人の座標がiさんよりも左である
            if x_pos > right_people[y_pos]:
                print("Yes")
                exit()

        # iさんと同じY座標にいて、同じように左を向いている人間がいる場合
        if y_pos in left_people:
            left_people[y_pos] = max(x_pos, left_people[y_pos])
        else:
            left_people[y_pos] = x_pos

print("No")
