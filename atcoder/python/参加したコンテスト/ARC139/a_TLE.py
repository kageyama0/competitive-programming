# 貪欲法的な感じ？前から決めていく

N = int(input())
T = list(map(int, input().split()))

now = int(bin(2**T[0]), 2) + 1
for i in range(1, N):
    Flag = True
    print(i, now)
    while Flag:
        b = bin(now)
        # print(b, now, b[-T[i]:], '0'*T[i])
        if T[i] == 0:
            if b[-1] == '1':
                print(b)
                Flag = False

        else:
            if b[-T[i]:] == '0'*T[i] and b[-T[i]-1] == '1':
                print(b)
                Flag = False
        now += 1

print(now-1)
