d, g = map(int, input().split())

scores = []
sum = []
for i in range(d):
    a, b = map(int, input().split())
    scores.append([a, b])
    sum.append((i + 1) * 100 * a + b)


def ans(goal, p_num):
    # print(goal, p_num)

    if p_num <= 0:
        return float("INF")

    # n: 解く問題数。一番スコアの高い問題を必要な分か、あるいは限界まで解く。
    n = min(int(goal / (100 * p_num)), scores[p_num - 1][0])

    # point: 全部解いた場合のボーナスを追加した点数
    if n == scores[p_num - 1][0]:
        point = sum[p_num - 1]

    # point: 一番スコアの高い問題をn問だけ中途半端に解いた場合の点数
    else:
        point = 100 * p_num * n

    # まだgoalに達していなかった場合、余っているポイントと次に高得点な問題のインデックスを再帰関数に放り込む
    if goal > point:
        n += ans(goal - point, p_num - 1)

    # 全く解かずに、次の問題に進むパターン
    return min(n, ans(goal, p_num - 1))


print(ans(g, d, 0))
