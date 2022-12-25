s = input()
R = [[] for _ in range(len(s))]

left = 0
for i in range(len(s)):
    si = s[i]
    if si == "(":
        # スライドさせる. [[x], [], ...] => [[], [x], ...]
        R[left + 1] = R[left]
        R[left] = []
        left += 1

    elif si == ")":
        # 消してスライドさせる. [[y], [x], ...] => [[x], [], ...]
        R[left] = []
        R[left-1] = R[left]
        left -= 1

    else:
        if si not in R[left]:
            R[left] += [si]
        else:
            print("No")
            exit()

    # print(i, si, R)


print("Yes")
