from collections import defaultdict

def main():
    s = input()
    n = len(s)
    ans = 0
    num = 0
    pow10 = 1
    d = defaultdict(int)
    d[0] = 1
    for i in reversed(range(n)):
        # pow10を10 ** (n-1-i)にしてるだけでTLEしていた
        pow10 = pow10 * 10 % 2019
        num += int(s[i]) * pow10
        mod = num % 2019
        ans += d[mod]
        d[mod] += 1
    print(ans)


if __name__ == "__main__":
    main()
