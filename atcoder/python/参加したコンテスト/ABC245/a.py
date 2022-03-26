A, B, C, D = map(int, input().split())

t_time = A * 60 + B
a_time = C * 60 + D

if t_time <= a_time:
    print("Takahashi")
else:
    print("Aoki")
