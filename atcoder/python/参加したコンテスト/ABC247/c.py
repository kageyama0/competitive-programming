N = int(input())

S = [None] * N
S[0] = "1"

for i in range(1, N):
    S[i] = S[i-1] + " " + str(i+1) + " " + S[i-1]

print(S[N-1])
# ans = []
# for x in S[N-1]:
#     ans.append(x)

# print(" ".join(ans))
