# https://atcoder.jp/contests/typical90/tasks/typical90_l
# union find(UF
h, w = map(int, input().split())
q = int(input())

grid = [[0] * (w+1) for _ in range(h+1)]

for _ in range(q):
    query = list(map(int, input().split()))
    print("----------")
    print(query)

    if query[0] == 1:
        ri, ci = query[1], query[2]
        grid[ri][ci] = 1
    else:
        rai, cai, rbi, cbi = query[1], query[2], query[3], query[4]

        if grid[rai][cai] != 1 or grid[rbi][cbi] != 1:
            print("No")
            continue

        flag1 = True
        for i in range(rai, rbi+1):
            if grid[i][j] != 1:
                flag1 = False
                break

        if flag1:
            print("Yes")
            continue

        flag2 = True
        for i in range(

        if flag1 and flag2:
            print("Yes")
        else:
            print("No")

    print(*grid, sep="\n")
