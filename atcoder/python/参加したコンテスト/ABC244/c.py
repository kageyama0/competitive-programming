N = int(input())
max = 2 * N + 1
nums = list(range(max))
print(max)

for _ in range(N):
    inp = int(input())
    nums.remove(inp)

    print(nums[-1])
    nums.remove(nums[-1])
