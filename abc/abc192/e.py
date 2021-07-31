import heapq
import math

n, m, x, y = map(int, input().split())
x, y = x-1, y-1

path = [[] for _ in range(n)]

for i in range(m):
    a, b, t, k = map(int, input().split())
    a, b = a-1, b-1
    path[a].append((b, t, k))
    path[b].append((a, t, k))

min_time = [float("inf") for _ in range(n)]

heap = [(0, x)]


while len(heap):
    # print(heap)
    time, town = heapq.heappop(heap)
    # print("town:", town, time)
    if min_time[y] < time:
        break
    for next, t, k in path[town]:
        next_time = ((time - 1) // k + 1) * k + t
        if min_time[next] > next_time:
            # print("add", next, next_time)
            min_time[next] = next_time
            heapq.heappush(heap, (next_time, next))

if math.isinf(min_time[y]):
    print(-1)
else:
    print(min_time[y])
