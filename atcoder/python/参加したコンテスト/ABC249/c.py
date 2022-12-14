# N < 15なので、ゴリゴリやる

from collections import defaultdict
from itertools import combinations

N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0

for i in range(K, N+1):
    comb = combinations(range(N), i)
    # c: N個の中からi個選ぶ組み合わせ
    for c in comb:
        d = defaultdict(int)
        # print(c)
        cnt = 0
        # 計算された組み合わせにあるインデックスを用いて、実際に数え上げる文字列を選択
        for index in c:
            # 実際の文字列を１つ１つ見ていく
            for st in S[index]:
                d[st] += 1

        # print(d)
        for val in d.values():
            if val == K:
                cnt += 1

        ans = max(ans, cnt)


print(ans)
