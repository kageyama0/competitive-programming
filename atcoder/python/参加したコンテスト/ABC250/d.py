import bisect
import math

import numpy as np

N = int(input())
if N < 54:
    print(0)
    exit()


def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2, N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum


NUMS = seachPrimeNum(10**6)

l = len(NUMS)
# print(l)

cnt = 0
for p_index in range(l-1):
    p = NUMS[p_index]
    close_to_q_num = math.ceil((N / p)**(1/3))
    q_index = bisect.bisect_left(NUMS, close_to_q_num)
    if q_index > p_index:
        while True:
            q = NUMS[q_index]
            if p * (q ** 3) <= N:
                break
            q_index -= 1

        cnt += q_index - p_index


print(cnt)
