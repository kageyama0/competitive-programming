import sys

readline = sys.stdin.readline

s = input()
q = int(input())

for _ in range(q):
    inp = readline().rstrip()
    if inp[0] == 1:
