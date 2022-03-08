s, t = input().split()
a, b = map(int, input().split())
u = input()

if s == u:
    print(a - 1, b)


if t == u:
    print(a, b - 1)
