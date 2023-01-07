n = int(input())
s = list(input())

# 書き換えフラグ、これがTrueの間は書き換えない
flag = True
for i in range(n):
    if s[i] == "\"":
        if flag:
            flag = False
        else:
            flag = True
    elif s[i] == "," and flag:
        s[i] = "."

print("".join(s))
