import math

N = int(input())

# ある程度当たりをつける。N付近になるような数を探す。
# Nが10^18までだから、a, bは10^6くらいまでのはず。
# a=b=10^6 => X=4*10^18
# a=0, b= 10^6 => X=10^18

# a,bの中でとりうる最小値からスタート
a = 0
# a=0なら、bは,int(n**(1/3))+1の数を使わなければならないはず...
b = int(N**(1/3))+1

ans = math.inf
while a <= b:
    # X = a^3 + a^2 * b + a * b^2 + b^3
    X = (a+b)*(a**2+b**2)
    if X >= N:
        ans = min(ans, X)
        b -= 1
    else:
        a += 1

print(ans)
