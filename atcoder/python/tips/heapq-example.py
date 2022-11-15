# 優先度付きキューを使う
from heapq import heapify, heappop, heappush

# ヒープに追加
heap = []
heappush(heap, 1)
heappush(heap, 3)
heappush(heap, 2)
print(heap)

# ヒープから取り出す
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))

# リストをヒープキューに変換
L = [1, 3, 2]
heapify(L)
print(heappop(L))
print(heappop(L))
print(heappop(L))
