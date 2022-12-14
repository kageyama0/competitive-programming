from fractions import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    m = 1
    for i in range(n):
        m = lcm(m, A[i])

    ans = 0
    for i in range(n):
        ans += (m / A[i]) % MOD
    print(ans)


if __name__ == "__main__":
    main()
