# 文字を前から決定していくタイプ
n = int(input())
alp = [chr(ord("a") + x) for x in range(26)]


def dfs(S):
    if len(S) == n:
        print(S)
    else:
        max_s = ord(max(S)) - 96
        # print(max_s)
        for i in range(max_s + 1):
            dfs(S + alp[i])


dfs("a")


# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# N = int(read())

# alphabets = [chr(ord("a") + x) for x in range(26)]

# print(alphabets)

# def dfs(S, i):
#     print(S)
#     if len(S) == N:
#         yield ''.join(S)
#         return

#     for j in range(i):
#         print("j:",j)
#         for w in dfs(S + [alphabets[j]], i):
#             print("i:",i,w)
#             yield w

#     # (i + 1)
#     for w in dfs(S + [alphabets[i]], i + 1):
#         print("i+1:",i+1,w)
#         yield w

# for w in dfs([], 0):
#     print(w)
