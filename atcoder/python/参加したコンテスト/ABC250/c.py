N, Q = map(int, input().split())

X_INDEX = [i for i in range(N+1)]
NUMS = [i for i in range(N+1)]

for _ in range(Q):
    x = int(input())
    x_index = X_INDEX[x]
    x_num = NUMS[x_index]

    y_index = x_index + 1 if x_index < N else x_index - 1
    # print(x_index, y_index, X_INDEX, NUMS)
    y_num = NUMS[y_index]
    NUMS[x_index] = y_num
    NUMS[y_index] = x_num
    X_INDEX[x_num] = y_index
    X_INDEX[y_num] = x_index

print(" ".join(map(str, NUMS[1:])))
