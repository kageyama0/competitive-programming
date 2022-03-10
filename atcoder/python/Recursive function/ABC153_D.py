n = int(input())
def f(n):
    if n == 1:
        return 1
    else:
        x = n//2
        time = 2 * f(x) + 1
        return time

print(f(n))
