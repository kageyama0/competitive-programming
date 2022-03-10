n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split())) + [l]

# 最小の羊羹がある長さ(length)よりも、何個に分けられるか？


def check(length):
    # 端に行くまでに分けれる数
    cnt = 0
    # スタート地点
    head = 0

    for a in A:
        if head + length <= a:
            head = a
            cnt += 1

    return cnt


ok, ng = 0, l//(k + 1) + 1
# ok + 1 = ngになったら、ループ終了
while ok + 1 < ng:
    # okとngの真ん中の値で行けるかどうかチェック
    half = (ok + ng) // 2
    if (check(half) >= k + 1):
        ok = half
    else:
        ng = half
print(ok)
