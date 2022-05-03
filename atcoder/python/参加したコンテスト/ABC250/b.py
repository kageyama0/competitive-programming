S = input()

upper = False
lower = False
set = set()
for s in S:
    if s.isupper():
        upper = True
    elif s.islower():
        lower = True

    set.add(s)


if upper and lower and len(set) == len(S):
    print("Yes")
else:
    print("No")
