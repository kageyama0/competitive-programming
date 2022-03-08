# 文字列の部分一致
import re

# ?があるとエラーが起きるので
# "."は、メタ文字（特別な意味を持つ文字）
# https://qiita.com/hiroyuki_mrp/items/29e87bf5fe46de62983c
s = input().replace('?', '.')
t = input()
#print("s,t:", s, t)

for i in range(len(s) - len(t), -1, -1):
    # re.match : 文字列の先頭がマッチするかチェック、抽出
    if re.match(s[i:i + len(t)], t):
        #print(s[i:i + len(t)], t)
        s = s.replace('.', 'a')
        print(s[:i] + t + s[i + len(t):])
        exit()

print('UNRESTORABLE')
