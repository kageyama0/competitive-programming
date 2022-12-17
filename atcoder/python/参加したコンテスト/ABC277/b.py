n = int(input())

str_0 = ["H", "D", "C", "S"]
str_1 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
L = [None]

ans = "Yes"
for i in range(n):
    s = input()
    if s[0] not in str_0 or s[1] not in str_1:
        ans = "No"

    if s in L:
        ans = "No"

    L.append(s)

print(ans)
