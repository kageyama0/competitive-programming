s = input()

if len(s) != 8:
    print("No")
    exit()

for i in range(8):
    if i == 0 or i == 7:
        if not s[i].isalpha():
            print("No")
            exit()
    else:
        if not s[i].isdigit():
            print("No")
            exit()

if 100000 <= int(s[1:7]) <= 999999:
    print("Yes")
else:
    print("No")
