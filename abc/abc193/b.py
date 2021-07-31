import math
n = int(input())
min_value = float("inf")
for _ in range(n):
    a, p, x = map(int, input().split())
    if x - a > 0:
        min_value = min(p, min_value)
if math.isinf(min_value):
    print(-1)
else:
    print(min_value)
