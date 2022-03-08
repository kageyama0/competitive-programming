import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def main():
    n = int(input())
    if n == 1:
        print(0)
        exit()

    d = collections.Counter(prime_factorize(n))
    #print(d)

    ans = 0
    for _, cnt in d.items():
        now = 1
        while cnt >= now:
            #print("cnt:",cnt,"now:",now)
            cnt -= now
            now += 1
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
