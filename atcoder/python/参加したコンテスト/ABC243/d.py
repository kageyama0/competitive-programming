from collections import deque


def culc(dir, x):
    if dir == "L":
        x *= 2

    elif dir == "R":
        x = x * 2 + 1

    else:
        x //= 2

    return x


n, x = map(int, input().split())
s = input()

if n == 1:
    culc(s, x)
    exit()

new_s = [s[0]]
for i in range(1, n):
    next = s[i]
    if len(new_s) > 0:
        print(">0", new_s)
        if (new_s[-1] == "R" or new_s[-1] == "L"):
            if next == "U":
                new_s.pop()
            else:
                new_s.append(next)

        else:
            new_s.append(next)

    else:
        new_s.append(next)

    print(new_s)

for dir in new_s:
    x = culc(dir, x)

print(x)
