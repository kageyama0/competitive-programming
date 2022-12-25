# 方針 : ひっくり返しても横との関係性は変わらないので、横との関係性を考える
# 次に、縦との関係性を考える

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
yoko_OK = [[] for _ in range(h)]
tate_OK = [[] for _ in range(h)]

for i in range(h):
    for j in range(w):
        now = j
        left = j-1

        if now in yoko_OK[i]:
            continue

        # 左端はスキップ
        if j == 0:
            continue

        else:
            # 横の関係性をチェック
            if A[i][now] == A[i][left]:
                yoko_OK[i].append(left)
                yoko_OK[i].append(now)


print(yoko_OK)

for i in range(h):
    for j in range(w):
        now = i
        up = i-1

        # 上端はスキップ
        if now == 0:
            continue

        # 横がOKならスキップ
        if j in yoko_OK[now]:
            # print("yoko_ok", i, j)
            continue

        else:
            print(now, up, j)
            if A[now][j] == A[up][j]:
                print("tate_ok", i, j)
                tate_OK[now].append(j)
                tate_OK[up].append(j)

print(tate_OK)
R = []

# 上から見ていく
for i in range(h):
    for j in range(w):
        if j in yoko_OK[i]:
            continue

        if j in tate_OK[i]:
            continue
