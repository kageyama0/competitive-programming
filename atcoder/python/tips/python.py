# open(0).read()

# 8 9
# 0 1 2
# 0 3 2
# 1 1 3
# 1 1 4
# 0 2 4
# 1 4 1
# 0 4 2
# 0 0 0
# 1 0 0
N, Q, *X = map(int, open(0).read().split())
print(X) # => [0, 1, 2, 0, 3, 2, 1, 1, 3, 1, 1, 4, 0, 2, 4, 1, 4, 1, 0, 4, 2, 0, 0, 0, 1, 0, 0]

#-----------------------------------------------------------------------------

# 内包表現
# こういうふうにして書くことで、不確定な個数の要素の中から最小値が取れる

for i in range(1, N):
    dp[i] = min(dp[j] + abs(h[i] - h[j]) for j in range(max(i - K, 0), i))

#-----------------------------------------------------------------------------

# ZIP関数
# 詳しくは、　https://note.nkmk.me/python-zip-usage-for/
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18

#-----------------------------------------------------------------------------

# 正規表現
# https://note.nkmk.me/python-re-match-search-findall-etc/
# match()は文字列の先頭がパターンにマッチするとマッチオブジェクトを返す。
# search()は文字列すべてが検索対象で、先頭にない文字列にもマッチする。match()と同じく、マッチする場合はマッチオブジェクトを返す。
import re

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

m = re.match(r'[a-z]+@[a-z]+\.com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

m = re.match(r'[a-z]+@[a-z]+\.net', s)
print(m)
# None

#-------------------------------------
m = re.search(r'[a-z]+@[a-z]+\.net', s)
print(m)
# <re.Match object; span=(26, 37), match='ccc@zzz.net'>

m = re.search(r'[a-z]+@[a-z]+\.com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

#---------------------------------------------------------------
# iter()

season = ['Spring', 'Summer', 'Fall', 'Winter']
iter_season = iter(season)
print(next(iter_season))
# 1番目のイテレータ(Spring)を表示後、次のイテレータ(Summer)に進む

next(iter_season)
# 次のイテレータ(Fall)に進む

# イテレータを１つずつ取り出して表示
for i in iter_season:
    print(i) # Winter

# イテレータを１つずつ取り出して表示。しかしうまく決まらなかった...イテレーターが最後まで進んでしまっているようだ...
for i in iter_season:
    print(i) # ...反応がないただの屍のようだ

# 結果
# <class 'list_iterator' >
# Spring
# Fall
# Winter

#-----------------------------------------------------------------------------
#itertools

from itertools import product
# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111

from itertools import groupby
# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

from itertools import repeat
# repeat(10, 3) --> 10 10 10
# list(map(pow, range(10), repeat(2)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

from itertools import zip_longest
# zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-



#---------------------------------------------------
#アルファベット
alp = [chr(ord("a") + x) for x in range(26)]
