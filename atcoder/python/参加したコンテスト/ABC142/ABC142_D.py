def isPrime(n):


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


def main():
    a, b = map(int, input().split())
    g = gcd(a, b)
    ans = [1]
    for i in range(2, g ** .5+1):


if __name__ == "__main__":
    main()
