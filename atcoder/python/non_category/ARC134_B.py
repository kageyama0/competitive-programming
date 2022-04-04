# 辞書順最小
# 貪欲法
# https://atcoder.jp/contests/arc134/tasks/arc134_b

N = int(input())
s = list(input())


# 入力値の文字列が辞書順で何番目のアルファベットで構成されているのかを、用いたアルファベットの個数で記録する
rest_alp_cnt = [0]*26
for i in range(N):
    rest_alp_cnt[ord(s[i])-97] += 1
# print(rest_alp_cnt)

# tempは、文字列sの中で、辞書順最小のアルファベットが何番目のアルファベットか？
for i in range(26):
    if rest_alp_cnt[i]:
        least_alp_num = i
        break




# 文字列sの先頭から順に、辞書順最小になるような入れ替えをしていく
# 位置p, qの文字を入れ替えたら、その次の入れ替えでは p < p'< q'< qとなるようなp', q'しか入れ替えられない。
# また、入れ替えるべきなのは辞書順最初のアルファベットのみであり、入れ替えようとしているものが辞書順最小のアルファベットかどうかさえわかれば良い。

p = 0
q = N-1
while q > p:
    # 入れ替えようとしている先頭のアルファベットが、辞書順最小のアルファベットの場合
    if ord(s[p])-97 == least_alp_num:
       # 使った分をrest_alp_cntから引いておく。
        rest_alp_cnt[ord(s[p])-97] -= 1

        # 入れ替え位置更新
        p += 1

        # 辞書順最小のアルファベットを使い切っていたなら、least_alp_numを更新する
        if rest_alp_cnt[least_alp_num] == 0:
            for i in range(least_alp_num+1, 26):
                if rest_alp_cnt[i]:
                    least_alp_num = i
                    break

    # 入れ替えようとしている最後尾のアルファベットが、辞書順最小のアルファベットの場合
    elif ord(s[q])-97 == least_alp_num:
        # 使った分をrest_alp_cntから引いておく。
        rest_alp_cnt[ord(s[p])-97] -= 1
        rest_alp_cnt[ord(s[q])-97] -= 1

        # 入れ替え
        s[q], s[p] = s[p], s[q]

        # 入れ替え位置更新
        p += 1
        q -= 1

        # 辞書順最小のアルファベットを使い切っていたなら、least_alp_numを更新する
        if rest_alp_cnt[least_alp_num] == 0:
            for i in range(least_alp_num+1, 26):
                if rest_alp_cnt[i]:
                    least_alp_num = i
                    break

    # pもqも辞書順最小のアルファベットでない場合
    else:
        rest_alp_cnt[ord(s[q])-97] -= 1
        q -= 1



print("".join(s))
