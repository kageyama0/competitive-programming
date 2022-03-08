// 桁DP
n = int(input())
k = input()

counter = defaultdict(int)

for x in map(str, range(1, n + 1)):
    head = x[0]
    tail = x[-1]
    counter[(head, tail)] += 1
print(counter)
