# https://atcoder.jp/contests/tdpc/tasks/tdpc_tournament

# 勝率計算
def win_prob_calc(Rq, Rp):
    win_prob = 1/(1 + 10**((Rq - Rp)/400))
    return win_prob


k = int(input())
num_people = 2**k
Rate = [int(input()) for _ in range(num_people)]
probs = [1] * num_people
for r in range(k):
    np = [0] * (num_people)

    for i in range(num_people):
        j = ((i >> r) ^ 1) << r
        print("i,r,j:", i, r, j)
        print("i>>r, (i>>r)^1", i >> r, (i >> r) ^ 1)
        for l in range(j, j + 2 ** r):
            np[i] += probs[l] * win_prob_calc(Rate[i], Rate[l])
        np[i] *= probs[i]
        print("r,np", r, np)

    probs = np
    print("probs:", probs)
    print("--------------------")

for prob in probs:
    print(f'{prob:.7f}')
