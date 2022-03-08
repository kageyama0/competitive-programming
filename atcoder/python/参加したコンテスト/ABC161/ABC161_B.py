n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = sum(a)

limit = s // (4*m)
for i in range(m):
    if a[i] < limit:
        print("No")
        exit()

print("Yes")
