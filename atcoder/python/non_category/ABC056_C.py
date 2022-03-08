import math

x = int(input())
x = abs(x)

# sum = sec(sec+1)/2
a = math.ceil((2 * x) ** (0.5))
s = a * (a+1) // 2

while s >= x:
    a -= 1
    s = a * (a+1) // 2

print(a+1)
