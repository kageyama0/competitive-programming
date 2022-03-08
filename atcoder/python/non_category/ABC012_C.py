n = int(input())
cnt = 2025
forget = cnt - n
for i in range(1, 10):
    n = forget // i
    if forget % i == 0 and n <= 9:
        n = forget // i
        print(str(i) + "x" + str(n))
