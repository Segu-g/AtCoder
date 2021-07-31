import heapq

q = int(input())
queries = tuple(tuple(map(int, input().split())) for _ in range(q))

output_buf = []

val_heap = []
offset = 0

for query in queries:
    if query[0] == 1:
        x = query[1]
        heapq.heappush(val_heap, x - offset)
    elif query[0] == 2:
        x = query[1]
        offset += x
    elif query[0] == 3:
        val = heapq.heappop(val_heap)
        output_buf.append(val + offset)

print("\n".join(map(str, output_buf)))
