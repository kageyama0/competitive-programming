n = int(input())


def calc_divisor(x):
    divisors = []
    for i in range(1, x+1):
        if x % i == 0:
            divisors.append(i)

    return divisors


def calc(x):
    if x == 1:
        return 1

    divisors = calc_divisor(x)
    # print(divisors)

    cnt = 0
    for d in divisors:
        if d == x:
            print(d)
            cnt += 1
        else:
            if x**2 // d <= n:
                print(d, x**2 // d)
                cnt += 2

    return cnt


ans = 0
for i in range(1, n+1):
    ans += calc(i)
    # print(f"ans:{ans}")

print(ans)
