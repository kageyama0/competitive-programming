N = int(input())
T = list(map(int, input().split()))

a = 0
for t in T:
    a = (a >> t) << t
    print("1","t", t, "a", a)
    a += 1 << t
    print("2","t", t, "a", a)
    if not a >> t & 1:
        a += 1 << t
        print("3","t", t, "a", a)

print(a)
