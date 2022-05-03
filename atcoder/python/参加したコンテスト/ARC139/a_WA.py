N = int(input())
T = list(map(int, input().split()))

now = T[0]
ans_digits_2 = T[0] + 1
for i in range(1, N):
    if T[i] >= now:
        ans_digits_2 = max(ans_digits_2 + 1, T[i] + 1)
    now = T[i]

if ans_digits_2 == T[-1] + 1:
    ans = "0b1" + "0" * T[-1]
elif ans_digits_2 == T[-1] + 2:
    ans = "0b11" + "0" * T[-1]
elif ans_digits_2 >= T[-1] + 3:
    ans = "0b1" + "0" * (ans_digits_2 - T[-1] - 2) + "1" + "0" * T[-1]

print(int(ans,2))
