# n 枚の帽子を持っている。i番目の帽子には番号ai
# n 頭のラクダが輪っかになっててそこに帽子をかぶせる
# 3 ^ 5 = 011 ^ 101 = 110

n = int(input())
A = list(map(int, input().split()))
num = 0
for a in A:
    num = num ^ a

if num == 0:
    print("Yes")
else:
    print("No")
