# 再帰関数
def find(x):
    if P[x] < 0:
        return x
    else:
        return find(P[x])


N, Q, *X = map(int, open(0).read().split())
# Pに繋がっている頂点の最終地点まで記録する
P = [-1] * N

for i in range(Q):
    i *= 3
    p, a, b = X[i], find(X[i + 1]), find(X[i + 2])
    if p == 1:
        print('Yes' if a == b else 'No')
    else:
        if a != b:
            if a > b:
                a, b = b, a
            P[b] = a
    print(P)

# from collections import deque
# n,q = map(int,input().split())

# link = [[] for _ in range(n)]
# judge = []
# # 頂点同士のつながりを記録
# for _ in range(q):
#     p, a, b = map(int, input().split())
#     if p == 0:
#       if not b in link[a]:
#         link[a].append(b)
#       if not a in link[b]:
#         link[b].append(a)
#     else:
#       judge.append([a,b])

# # print(link,judge)
# # [[0], [2], [1, 3, 4], [2], [2], [], [], []] [[1, 3], [1, 4], [4, 1], [0, 0]]
# for j_a, j_b in judge:
#     l = link
#     s = deque()
#     s.append(j_a)
#     while s:
#         now = s.pop()
#         if j_b in l[now]:
#             print("Yes")
#             break
#         else:
#             for i in l[now]:
#                 s.append(i)
#             l[now] = []
#     print("No")
