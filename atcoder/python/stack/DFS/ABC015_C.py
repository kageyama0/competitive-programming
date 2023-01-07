n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

nums = t[0]
A = []
for i in range(1, n):
    for x in t[i]:
        for y in nums:
            # print(nums,A)
            A.append(int(x ^ y))
    nums += A

if 0 in nums:
    print("Found")
else:
    print("Nothing")


# def dfs(numQ, ans):
#     if numQ == N:
#         return ans == 0
#     for i in range(K):
#         if(dfs(numQ+1, ans ^ T[numQ][i])):
#             return True


# print("Found" if dfs(0, 0) else "Nothing")
