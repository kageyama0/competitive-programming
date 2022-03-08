d, g = map(int, input().split())

scores = []
sum = []
for i in range(d):
    a, b = map(int, input().split())
    scores.append([a, b])
    sum.append((i + 1) * 100 * a + b)

def ans(goal, p_num):
    if p_num <= 0:
        return float("INF")

    # 一番スコアの高い問題を必要な分か、あるいは限界まで解く。
    n = min(int(goal / (100 * p_num)), scores[p_num - 1][0])

    # できる限りまで高得点問題を解いたときの特典
    s = 100 * p_num * n

    # 全部解いたら、ボーナスを追加した点数を s とする
    if n == scores[p_num - 1][0]:
        s = sum[p_num - 1]

    # まだgoalに達していなかった場合、再帰関数に放り込む
    if goal > s:
        n += ans(goal - s, p_num - 1)

    return min(n, ans(goal, p_num - 1))

print(ans(g, d))
