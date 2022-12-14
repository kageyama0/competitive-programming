# TODO: これは間違い解答なので、要修正

N, M = map(int, input().split())
A = list(map(int, input().split())) + [0] * (M+1)
C = list(map(int, input().split()))
B = [0] * (N+M+1)

# Aの中で、一番インデックスが小さくて、かつ0じゃない部分を探すところから。
x = 0
for i in range(N+1):
    if A[i] != 0:
        x = i


for i in range(x+M+1):
    # Ci = A0Bi + A1Bi-1 + .... + AiB0 だから
    # Bi = (Ci - A1Bi-1 + .... + AiB0 ) / A0
    # この A1Bi-1 + .... + AiB0 をcntとする

    if i >= x:
        cnt = 0
        for j in range(i):
            cnt += A[i-j] * B[j]

        # A[0] == 0 だとバグっちゃうから注意
        print(i-x, i, x)
        B[i-x] = (C[i] - cnt) // A[x]
        print(C[i], cnt, B, B[i])

print(" ".join(map(str, B[:M+1])))
