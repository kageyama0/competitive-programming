# まあ、これは縦と横の和を求めて、最後に各々の値を引くだけ

h, w = map(int, input().split())

A = [None]*(h)
rows = [0]*(h)
for i in range(h):
    row_nums_list = list(map(int, input().split()))
    rows[i] = sum(row_nums_list)
    A[i] = row_nums_list

columns = [0]*(w)
for i in range(w):
    column_sum = 0
    for j in range(h):
        column_sum += A[j][i]
    columns[i] = column_sum

for i in range(h):
    ans = []
    for j in range(w):
        ans.append(rows[i] + columns[j] - A[i][j])
    print(" ".join(map(str, ans)))
