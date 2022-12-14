s1, s2, s3 = input().split()
t1, t2, t3 = input().split()

# print(s1,s2,s3)

even_pattern = [(s1, s2, s3), (s2, s3, s1), (s3, s1, s2)]

if (t1, t2, t3) in even_pattern:
    print("Yes")
else:
    print("No")
