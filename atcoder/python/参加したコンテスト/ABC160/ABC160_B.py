#
x = int(input())
num_1 = x // 500
num_2 = (x - num_1 * 500) // 5

ans = num_1 * 1000 + num_2 * 5
print(ans)
