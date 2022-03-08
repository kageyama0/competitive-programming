b = list(input().split())
n = int(input())
a = [input() for _ in range(n)]

#{与えられた数字: 大きさの評価}
rep_dict = {n:str(i) for i, n in enumerate(b)}

def replace_dict(s, d):
  if s == "0":
    return 0
  result = ""
  for c in s:
    result += d[c]
  return int(result)

#sortの「key = lambda x : ...」ってやつは、結局何を参考にソートするか決めるもの
#つまり、リストの一つ一つの値がxの中に収納され、それに対応してその大きさを評価する関数を作り、その関数がはじき出した評価を元にソートしてくれる
# また、いつも二次元配列をソートするときに、「key = lambda x: x[1]」としているのは、渡すことになるものがリストだから！
# [1,0]などの...
print("\n".join(list(sorted(a, key = lambda x: replace_dict(x, rep_dict)))))
