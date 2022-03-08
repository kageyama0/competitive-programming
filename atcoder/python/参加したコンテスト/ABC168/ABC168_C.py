import math
import numpy
a, b, h, m = map(int, input().split())

# h *= 30
# m *= 6
# d = abs(h - m)
# dif = min(360 - d, d)
# rad = math.radians(dif)
# ans = (a ** 2 + b ** 2 - 2 * a * b * (math.cos(rad)))**(0.5)
# print(ans)

h_r = math.radians((h * 30))
m_r = math.radians((m * 6))
h_v = np.array([math.cos(h_r), math.sin(h_r)]) * a
m_v = np.array([math.cos(h_r), math.sin(h_r)]) * b
ans = (a ** 2 + b ** 2 - 2 * np.dot(h_v, m_v))**(0.5)
print(ans)
