n = int(input())

print(1)


if n == 2:
    print(1, 1)

elif n >= 3:
    print(1, 1)
    L = [1, 1]
    l = 2
    while l < n:
        new_L = [1] + [None] * (l - 1) + [1]
        for i in range(1, l):
            new_L[i] = L[i-1] + L[i]

        L = new_L
        l = len(L)
        print(*L)
