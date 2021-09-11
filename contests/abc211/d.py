import heapq
from typing import Optional, Set, List, Tuple

MOD = 10 ** 9 + 7

n, m = map(int, input().split())
edges: List[Set[int]] = [set() for _ in range(n)]

for a, b in (map(int, input().split()) for _ in range(m)):
    a, b = a - 1, b - 1
    edges[a].add(b)
    edges[b].add(a)

vertex_heapq: List[Tuple[int, int]] = [(0, 0)]
vertex_state: List[Tuple[Optional[int], int]] = [(None, 0) for _ in range(n)]  # (cost, num)
vertex_state[0] = (0, 1)

while len(vertex_heapq) != 0:
    cost, vertex = heapq.heappop(vertex_heapq)
    _, case = vertex_state[vertex]
    if vertex == n - 1:
        break

    # print(vertex, cost, vertex_heapq)
    # print(vertex_state)

    for next_vertex in edges[vertex]:
        next_cost, next_case = vertex_state[next_vertex]

        if next_cost is None:
            heapq.heappush(vertex_heapq, (cost + 1, next_vertex))
            vertex_state[next_vertex] = (cost + 1, case)

        elif next_cost == cost + 1:
            vertex_state[next_vertex] = (cost + 1, (next_case + case) % MOD)

print(vertex_state[n - 1][1])
