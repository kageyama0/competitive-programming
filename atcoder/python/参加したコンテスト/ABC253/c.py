# やること
# 数字の個数をカウントする => 辞書型で個数をカウントする
# 数字を削除すること => 優先度付きキューを使う(最大値を把握するには-1をかけることで対応する)

from collections import Counter
from heapq import heappop, heappush

q = int(input())

# これで、0 ~ 10 ** 9までの個数をカウントする
cnt = Counter()

# 最小値、最大値を管理する
max_num_q = []
min_num_q = []


for _ in range(q):
    q_list = list(map(int, input().split()))
    # print(q_list)

    if q_list[0] == 1:
        x = q_list[1]
        cnt[x] += 1
        heappush(max_num_q, -x)
        heappush(min_num_q, x)
        # print(cnt, max_num_q, min_num_q)

    elif q_list[0] == 2:
        x, c = q_list[1], q_list[2]
        cnt[x] = max(0, cnt[x] - c)
        # ここで、カウントを減らした数字をヒープキューから取り除く必要はない
        # 結局、計算するときに最大値、最小値が分かれば良いので、関係ない値を取り除く処理をする必要がない
        # また、ヒープキューは特定の値を取り除くことができないので、その点でも無駄がある

    else:
        # 最大値、最小値のカウントが０であれば、取り除く
        while cnt[-max_num_q[0]] == 0:
            heappop(max_num_q)
        while cnt[min_num_q[0]] == 0:
            heappop(min_num_q)

        print(-max_num_q[0]-min_num_q[0])
