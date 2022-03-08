from collections import deque
import sys
buf = sys.stdin.buffer

h, w = map(int, buf.readline().split())
magic = deque()
max_eff = 0
# A:攻撃力, B:魔力
for _ in range(w):
    a, b = map(int, buf.readline().split())
    eff = a / b
    if max_eff < eff:
        max_eff = eff
        magic.append((a, b))
    else:
        magic.appendleft((a, b))

cnt = 0
m_a, m_b = magic.pop()
while h > 0:
    h -= m_a
    cnt += m_b
