# 1桁 --> 同じ数　1 * 9
# 2桁 --> (××,××)、(×,××) or (××,×) 9 * 3 = 27 / (△×,×△) 9*9-9 = 72
# 3桁 --> (×△×,×□×)、(×△×,××) or (××,×□×), (×,×□×) or (×□×,×)
import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


n = int(read())

counter = defaultdict(int)

for x in map(str, range(1, n + 1)):
    head = x[0]
    tail = x[-1]
    counter[(head, tail)] += 1
print(counter)

answer = 0
items = list(counter.items())
for (head, tail), cnt in items:
    answer += cnt * counter[(tail, head)]

print(answer)
