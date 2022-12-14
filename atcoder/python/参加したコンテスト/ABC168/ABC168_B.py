k = int(input())
s = input()
l = len(s)
if l > k:
    print(s[:k]+"...")
else:
    print(s)
