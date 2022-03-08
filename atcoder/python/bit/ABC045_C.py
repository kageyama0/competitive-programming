#https://atcoder.jp/contests/abc045/tasks/arc061_a

s = input()
cnt = len(s)-1
ans = 0
for i in range(2 ** cnt):
    # sign = ["", ... , ""] : +を入れるか否か
    sign = [""] * cnt

    for j in range(cnt):
        if (i >> j & 1):
            sign[j] = "+"
            
    formula = ""
    for k in range(cnt):
        formula += s[k] + sign[k]
    formula += s[cnt]
    ans += eval(formula)
print(ans)
