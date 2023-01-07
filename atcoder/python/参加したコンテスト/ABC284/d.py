t = int(input())


def prime_factorize(n):
    """
    素因数分解
    """
    f = 2
    while f * f <= n and n % f != 0:
        f += 1

    pq = n // f
    if pq % f == 0:
        p, q = f, pq // f
    else:
        p, q = int(pq ** 0.5), f

    return p, q


for _ in range(t):
    n = int(input())
    p, q = prime_factorize(n)
    print(p, q)
