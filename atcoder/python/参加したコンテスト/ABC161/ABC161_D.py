k = int(input())
cand = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
for _ in range(9):  # 上記の操作を9回繰り返せば10^5個以上のルンルン数を列挙できる
    tmp = []
    for val in cand[-1]:
        if val % 10 != 0:  # 末尾が0のときは(末尾-1)を付け加えた数はルンルン数にならない
            tmp.append(val * 10 + (val % 10 - 1))

        tmp.append(val * 10 + (val % 10))

        if val % 10 != 9:  # 末尾が9のときは(末尾+1)を付け加えた数はルンルン数にならない
            tmp.append(val * 10 + (val % 10 + 1))

    cand.append(tmp)

ans = []
for i in range(len(cand)):
    for val in cand[i]:
        ans.append(val)
ans = sorted(ans)
print(ans[k-1])
