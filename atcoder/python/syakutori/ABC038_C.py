N = int(input())
A = list(map(int, input().split()))

left, right, ans = 0, 1, N
while left != N:
    while right != N and A[right-1] < A[right]:
        right += 1

    if left + 1 != right:
        length = right - left
        ans += length * (length - 1) // 2

    # print("left:", left, "right:", right, "ans:", ans)
    left = right
    right = left + 1


print(ans)
