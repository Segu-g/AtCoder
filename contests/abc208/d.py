from collections import defaultdict
import math
import heapq

n, m = map(int, input().split())

paths = [dict() for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    paths[a][b] = c
