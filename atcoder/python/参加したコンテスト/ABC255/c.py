x, a, d, n = map(int, input().split())


# Xが初項より小さければ、初項よりもn-xが答え
if x <= a:
    print(n - a)
    exit()

# 一番大きい項
if a + d * (n-1) <= x:
    print(x - a - d * (n-1))
    exit()


n_x = (x - a) // d
