from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
sum_A = 0
# カードの枚数をカウントしつつ、全体の合計も計算する
for a in A:
    d[a] += 1
    sum_A += a

# カードの数字を小さい順に並べる
card_nums = []
for k, v in d.items():
    card_nums.append(k)
sorted_card_nums = sorted(card_nums)

# 取り除けるカードの合計の最大値
max_remove_sum = 0
# 今のカードの合計
now_sum = sorted_card_nums[0] * d[sorted_card_nums[0]]

for i in range(1, len(sorted_card_nums)):
    prev = sorted_card_nums[i-1]
    next = sorted_card_nums[i]
    # print(prev, next)
    if next - prev <= 1:
        now_sum += next * d[next]

    else:
        max_remove_sum = max(now_sum, max_remove_sum)
        now_sum = next * d[next]

    # print("max_remove_sum, now_sum", max_remove_sum, now_sum)


# (0, 1, 2, ..., m-1)みたいに頭とお尻が繋がるパターンも考慮する
# m-1までのカードを使った時の合計はnow_sumに入っているので、それを使う
if m - 1 in d:
    for i in range(len(sorted_card_nums)):
        if i in d:
            now_sum += i * d[i]
        else:
            break

max_remove_sum = max(now_sum, max_remove_sum)

# 最初から最後までずっと単調増加だった場合は、0未満になってしまうので、0にする
print(sum_A - max_remove_sum if sum_A - max_remove_sum >= 0 else 0)
