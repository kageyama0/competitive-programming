n, k, m, r = map(int, input().split())
s = [int(input()) for _ in range(n - 1)]
s.sort(reverse=True)

sum_s = sum(s[:k-1])
dif = r * k - sum_s

if sum(s[:k]) >= r * k:
    print(0)
else:
    if dif > m:
        print(-1)
    else:
        print(dif)
