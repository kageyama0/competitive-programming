from collections import deque

Q = int(input())

q = deque([])

for _ in range(Q):
    query = list(map(int, input().split()))
    # [xの球、n個]
    if query[0] == 1:
        q.append([query[1], query[2]])

    elif query[0] == 2:
        c = query[1]

        cnt = 0
        while c > 0:
            # print("取り出したい球の数:", c)

            p = q.popleft()
            p_x = p[0]
            p_c = p[1]
            # print("取り出そうとしている球:", p_x)
            # print("取り出そうとしている球の個数:", p_c)

            # 取り出そうとしている球よりも連続していれたXの数の方が多い場合
            if p_c > c:
                cnt += p_x * c
                print(cnt)
                q.appendleft([p_x, p_c-c])
                break

            # ちょうど同じ場合
            elif p_c == c:
                cnt += p_x * p_c
                print(cnt)
                break

            # 取り出そうとしている球よりも連続していれたXの数の方が少ない場合
            else:
                cnt += p_x * p_c
                c -= p_c

            # print("cnt",cnt)
