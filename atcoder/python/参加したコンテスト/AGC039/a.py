# https://atcoder.jp/contests/agc039/tasks/agc039_a

s = input()
n = len(s)
k = int(input())

C = [1]
now_s = s[0]
for i in range(1, n):
    if s[i] == now_s:
        C[-1] += 1
    else:
        C.append(1)
        now_s = s[i]
# print(C)

# 先頭と末尾が同じじゃない時は、全部足してk倍するだけ
if s[0] != s[-1]:
    ans = sum(c // 2 for c in C) * k
else:
    if len(C) == 1:
        ans = C[0] * k // 2
    else:
        # 先頭と末尾の分をカウントする
        ans = C[0] // 2 + C[-1] // 2
        # (k-1)回出現する文字の先頭と末尾がくっつく部分に関する計算をする
        ans += ((C[0] + C[-1]) // 2) * (k - 1)
        # 残りの文字列に関する計算をする
        ans += sum(c // 2 for c in C[1:-1]) * k

print(ans)
