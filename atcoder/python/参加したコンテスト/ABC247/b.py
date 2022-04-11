N = int(input())
st = [input().split() for _ in range(N)]
# print(st)


for i in range(N):
    a = st[i][0]
    b = st[i][1]
    used = []
    # 他の人の名前とかぶっていないかチェック
    for j in range(N):
        if i == j:
            continue

        c = st[j][0]
        d = st[j][1]
        used.append(c)
        used.append(d)
        if a in used and b in used:
            print("No")
            exit()

print("Yes")
