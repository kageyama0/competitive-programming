A, B = map(int, input().split())

if A == 0:
    print(0, 1)

else:
    x = ((A**2)/(A**2+B**2))**0.5
    y = B*x/A
    print(x, y)
