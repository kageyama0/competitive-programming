#

from fractions import gcd

n, a, b = map(int, input().split())


def calc(r):
    if r < n:
        x = n // r
        r_sum = r * (x * (x + 1)) // 2
        # print(x, r_sum)
        return r_sum
    else:
        return 0


all_sum = (n+1) * n // 2
a_sum = calc(a)
b_sum = calc(b)
# 最小公倍数
a_b_sum = calc(a*b // gcd(a, b))
ans = all_sum - a_sum - b_sum + a_b_sum
print(ans)
