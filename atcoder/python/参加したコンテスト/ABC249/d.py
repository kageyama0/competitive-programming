from collections import Counter


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
A = list(map(int, input().split()))
c = dict(Counter(A))
# print(c)

cnt = 0
for i in range(N):
    divs = make_divisors(A[i])
    for div in divs:
        cnt += c.get(div, 0) * c.get(A[i]//div, 0)
print(cnt)
