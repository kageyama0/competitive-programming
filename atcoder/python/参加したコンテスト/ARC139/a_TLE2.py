N = int(input())
T = list(map(int, input().split()))

now = T[0]
ans_digits_2 = T[0] + 1
ans = ["1"] + ["0"] * T[0]
for i in range(1, N):
    # print(now,ans)
    if T[i] >= now:
        ans_digits_2 = max(ans_digits_2 + 1, T[i] + 1)
        ans = ["1"] + ["0"] * (ans_digits_2 - 1)
        ans[-T[i]-1] = "1"
    else:
        ans[-T[i]-1] = "1"

    now = T[i]
# print(ans)
ans = "0b" + "".join(ans)
print(int(ans,2))
