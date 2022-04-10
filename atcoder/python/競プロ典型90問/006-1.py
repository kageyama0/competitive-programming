# https://atcoder.jp/contests/typical90/tasks/typical90_f
# 参考: https://github.com/E869120/kyopro_educational_90/blob/main/sol/006.cpp
# 辞書順に文字を決める
# 方針：桁DP
n, k = map(int, input().split())
S = list(input())
nex = [[0] * 26 for _ in range(n+1)]
for i in range(26):
    nex[n][i] = n
print(nex)

for i in range(n-1, -1, -1):
    for j in range(26):
        if (ord(S[i])-ord("a") == j):
            nex[i][j] = i
        else:
            nex[i][j] = nex[i+1][j]
print(*nex,sep="\n")

ans = ""
current_pos = 0
for i in range(1, k+1):
    for j in range(26):
        nex_pos = nex[current_pos][j]
        max_possible_length = n - nex_pos - 1 + i
        if max_possible_length >= k:
            ans += chr(ord("a") + j)
            current_pos = nex_pos + 1
            break

print(ans)



# ボツ
# これだと、最も辞書順で小さいアルファベットをなるべく使っている

# # どの文字をどこまで使うべきか？
# cnt = k
# ANS = [None] * n
# for i in range(26):
#     alp_cnt = len(alp_indexes[i])
#     print(alp[i], k, alp_cnt, alp_indexes[i])
#     if k >= alp_cnt:
#         k -= alp_cnt
#         for index in alp_indexes[i]:
#             ANS[index] = S[index]
#     else:
#         for index in alp_indexes[i][:k]:
#             ANS[index] = S[index]
#         break

# # Noneを省くための処理...なんかださい
# ans = ""
# for i in range(n):
#     if ANS[i] != None:
#         ans += ANS[i]

# print(ans)
