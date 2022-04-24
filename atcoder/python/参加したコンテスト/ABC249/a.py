A, B, C, D, E, F, X = map(int, input().split())

t_cnt, s_cnt = 0, 0
t_time, s_time = X, X

while t_time > 0:
    if t_time >= A:
        t_time -= A
        t_cnt += A * B
    else:
        t_cnt += t_time * B
        t_time = 0

    t_time -= C

while s_time > 0:
    if s_time >= D:
        s_time -= D
        s_cnt += D * E
    else:
        s_cnt += s_time * E
        s_time = 0

    s_time -= F


# print(t_cnt, s_cnt)
if t_cnt > s_cnt:
    print("Takahashi")
elif t_cnt < s_cnt:
    print("Aoki")
else:
    print("Draw")
