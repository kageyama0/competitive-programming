k = int(input())
alp = [chr(ord("A") + x) for x in range(26)]
print(*alp[:k], sep="")
