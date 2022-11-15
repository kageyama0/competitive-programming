a, b, c = map(int, input().split())
L = [a, b, c]
L.sort()
if L[1] == b:
    print("Yes")
else:
    print("No")
