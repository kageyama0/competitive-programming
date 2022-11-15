# これだとTLEになる

n, k = map(int, input().split())
A = list(map(int, input().split()))
# 実現すべき配列
B = sorted(A)

# Bの最初の要素から順番に調べていく
for i in range(n):
    # Bのi番目の要素が、i - 2k, i - k, i , i + 2k, i + 3k, ... にあるかどうかを調べる
    cnt_less_than_i = i // k
    cnt_greater_than_i = (n - i - 1) // k
    min_index = i - cnt_less_than_i * k
    max_index = i + cnt_greater_than_i * k
    # print(f"min_index:{min_index}, max_index:{max_index}")

    cnt = cnt_less_than_i + cnt_greater_than_i + 1
    all_diff = True
    for j in range(cnt):
        index = min_index + j * k
        if B[i] == A[index]:
            all_diff = False
            continue

    if all_diff:
        print("No")
        exit()

print("Yes")
