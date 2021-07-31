import heapq
n = int(input())
v_array = list(map(int, input().split()))
heap = []
for i in range(n):
    left, right = v_array[n - 1 - i], v_array[n + i]
    heapq.heappush(heap, left)
    heapq.heappush(heap, right)
    heapq.heappop(heap)
print(sum(heap))
