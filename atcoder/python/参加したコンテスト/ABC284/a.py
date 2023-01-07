n = int(input())
S = [ input() for _ in range(n) ]
print(*S[::-1], sep='\n')
