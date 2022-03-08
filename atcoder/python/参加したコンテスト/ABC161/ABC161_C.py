import math
n, k = map(int, input().split())

if n < k:
    if n > k / 2:
        print(k - n)
    else:
        print(n)
else:
    s = math.ceil(n / k)
    ans = abs(n - s  * k)
    while True:
        x = abs(ans - k)
        if x > ans:
            break
        else:
            ans = x
    print(ans)
