from collections import Counter, defaultdict


def calc_num_type(all_num_type, cnt_ij, cnt, h, w):
    """
    [i,j]が塗りつぶす部分の左上の座標のときの、数字の種類の数を計算する
    """
    ans = all_num_type
    for num, count in cnt_ij.items():
        if cnt[num] == count:
            ans -= 1
    return ans


H, W, N, h, w = map(int, input().split())

cnt = defaultdict(int)
grid = [[None] * W for _ in range(H)]
for i in range(H):
    A = list(map(int, input().split()))
    for a in A:
        cnt[a] += 1
    grid[i] = A

all_num_type = len(cnt)


# cnt_ij: [i, j]が塗りつぶす部分の左上の座標のときの、塗りつぶす数字の種類の数
cnt_ij = [[defaultdict(int)] * (W - w + 1) for _ in range(H - h + 1)]
cnt_00 = defaultdict(int)
for i in range(h):
    for j in range(w):
        cnt_00[grid[i][j]] += 1
cnt_ij[0][0] = cnt_00

# 左端の列の個数をカウントしておく
for i in range(1, H - h + 1):
    # 一つ上の列の個数をコピー
    cnt_ij[i][0] = cnt_ij[i - 1][0].copy()

    # 一つ上の列の個数から、増えた数を引く
    for j in range(w):
        # print(i, j)
        cnt_ij[i][0][grid[i - 1][j]] -= 1
        cnt_ij[i][0][grid[i + h - 1][j]] += 1

# print(*cnt_ij, sep="\n")


for k in range(H - h + 1):
    ANS = []
    for l in range(W - w + 1):
        if l == 0:
            ANS.append(calc_num_type(all_num_type, cnt_ij[k][l], cnt, h, w))
            continue

        # 一つ左の列の個数をコピー
        cnt_ij[k][l] = cnt_ij[k][l - 1].copy()

        # 一つ左の列の個数から、増えた数を引く
        for i in range(h):
            cnt_ij[k][l][grid[k + i][l - 1]] -= 1
            cnt_ij[k][l][grid[k + i][l + w - 1]] += 1

        ANS.append(calc_num_type(all_num_type, cnt_ij[k][l], cnt, h, w))

    print(*ANS)
